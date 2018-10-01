echo -n $1 |openssl dgst -sha256 -binary  | xxd -p -c 256 >hashLogin.txt
echo -n $2 |openssl dgst -sha256 -binary  | xxd -p -c 256 >hashPassword.txt

