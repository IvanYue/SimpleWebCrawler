

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            # fout.write(r"<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>")
            fout.write("<tr>")
            titlt =  data['title']
            summary = data['summary']
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % titlt)
            fout.write("<td>%s</td>" % summary)

            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        # fout.close()