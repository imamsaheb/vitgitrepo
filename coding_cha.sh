python3 -m unittest unit_coding_challenge.py
python3 coding_challenge.py
mv users.html users_$BUILD_NUMBER.html
scp users_$BUILD_NUMBER.html ec2-user@172.31.5.104:/usr/share/nginx/html/
mv users_pdf.pdf users_pdf_$BUILD_NUMBER.pdf
scp users_pdf_$BUILD_NUMBER.pdf ec2-user@172.31.5.104:/usr/share/nginx/html/

echo "click the link to download the html report, http://ec2-52-66-255-160.ap-south-1.compute.amazonaws.com:80/users_$BUILD_NUMBER.html"
echo "click the link to download the pdf report, http://ec2-52-66-255-160.ap-south-1.compute.amazonaws.com:80/users_pdf_$BUILD_NUMBER.pdf"
