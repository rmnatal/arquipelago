<?php
// Envolve cada declaração de função de nível superior em if ( ! function_exists() ) { ... }
$src = file_get_contents($argv[1]);
$code = "<?php\n" . $src;
$tokens = token_get_all($code);
$out = ''; $i = 0; $n = count($tokens); $depth = 0; $names = [];
while ($i < $n) {
    $t = $tokens[$i];
    if (is_array($t) && $t[0] === T_FUNCTION && $depth === 0) {
        $j = $i + 1; while (is_array($tokens[$j]) && $tokens[$j][0] === T_WHITESPACE) $j++;
        if (is_array($tokens[$j]) && $tokens[$j][0] === T_STRING) {
            $name = $tokens[$j][1]; $names[] = $name;
            $buf = ''; $k = $i; $d = 0; $started = false;
            while ($k < $n) {
                $tk = $tokens[$k]; $s = is_array($tk) ? $tk[1] : $tk; $buf .= $s;
                if ($s === '{') { $d++; $started = true; }
                elseif ($s === '}') { $d--; if ($started && $d === 0) { $k++; break; } }
                $k++;
            }
            $out .= "if ( ! function_exists( '$name' ) ) {\n" . $buf . "\n}";
            $i = $k; continue;
        }
    }
    $s = is_array($t) ? $t[1] : $t;
    if ($s === '{') $depth++; elseif ($s === '}') $depth--;
    $out .= $s; $i++;
}
$out = preg_replace('/^<\?php\n/', '', $out, 1);
file_put_contents($argv[2], $out);
fwrite(STDERR, "funções protegidas: " . implode(', ', $names) . "\n");
