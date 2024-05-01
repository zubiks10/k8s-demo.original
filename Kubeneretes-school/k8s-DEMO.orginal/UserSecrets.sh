set -x

touch ~/Desktop/k8s/Kubeneretes-school/k8s-DEMO/decode-user
touch ~/Desktop/k8s/Kubeneretes-school/k8s-DEMO/decode-pwd
echo -n mongouser | base64 > decode-user	
echo -n mongopasswd | base64 > decode-pwd


###encode the Values"The command `echo -n mongouser | base64` is used to encode the string "mongouser" in Base64 encoding without a newline character. When you run this command, it will produce the Base64 encoded representation of "mongouser.".####
