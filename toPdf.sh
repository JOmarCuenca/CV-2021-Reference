readarray -d / -t strarr <<< $1

dir=${strarr[0]}
file=${strarr[1]}

readarray -d . -t fileParts <<< $file

filename=${fileParts[0]}

cd $dir
jupyter nbconvert --to html $file
wkhtmltopdf "$filename.html" "$filename.pdf"

if [[ $2 != "-v" ]]; then
    rm "$filename.html"
fi