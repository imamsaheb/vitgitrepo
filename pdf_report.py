import sys
import pdfkit
build_number = sys.argv[0]
pdf1 = 'users_pdf_' + build_number + ".pdf"
url1 = 'http://ec2-52-66-255-160.ap-south-1.compute.amazonaws.com:80/users_' + build_number + ".html'
pdfkit.from_url(url1, pdf1)
