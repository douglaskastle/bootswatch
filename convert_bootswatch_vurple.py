import re
import os

values = { 
    'uc': 'Vurple',
    'lc': 'vurple',
    'cl': '#116BB7',
}
def main():
    infile = "yeti/variables.less"
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    outfile = values['lc'] + "/variables.less"
    f = open(outfile, 'w')
    for line in lines:
        line = re.sub('Yeti', values['uc'], line)
        line = re.sub('yeti', values['lc'], line)
        line = re.sub('#008cba', values['cl'], line)
        line = re.sub('headings-font-family:    @font-family-base', 'headings-font-family:    @font-family-header-sans-serif', line)
        if re.search("Open Sans", line):
            line = re.sub('Open Sans', 'Lato', line)
            line = '@font-family-header-sans-serif:  "Orbitron", "Helvetica Neue", Helvetica, Arial, sans-serif;\n' + line
        f.write(line)
    f.close()

    infile = "yeti/bootswatch.less"
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    outfile = values['lc'] + "/bootswatch.less"
    f = open(outfile, 'w')
    for line in lines:
        line = re.sub('Yeti', values['uc'], line)
        if re.search("Open\+Sans", line):
            continue
        if re.search("web-font-path", line):
            line = '@web-font-path2: "https://fonts.googleapis.com/css?family=Lato:400,700,400italic";\n' + line
            line = '@web-font-path: "https://fonts.googleapis.com/css?family=Orbitron:300italic,400italic,700italic,400,300,700";\n' + line
            line = line + '.web-font(@web-font-path2);\n'
        
        f.write(line)
    f.close()

    infile = "yeti/index.html"
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    outfile = values['lc'] + "/index.html"
    f = open(outfile, 'w')
    for line in lines:
        line = re.sub('Yeti', values['uc'], line)
        line = re.sub('yeti', values['lc'], line)
        line = re.sub('UA-[0-9\-]+', '', line)
        f.write(line)
    f.close()
    
    cmd = "/cygdrive/c/Users/keeshand/AppData/Roaming/npm/grunt swatch:{0}".format(values['lc'])
    os.system(cmd)
    
    cmd = "cp {0}/bootstrap.min.css ../vurple_com/pelican-themes/bootstrap3/static/css/bootstrap.{0}.min.css".format(values['lc'])
    os.system(cmd)
    
    cmd = "cp bower_components/font-awesome/css/*.css ../vurple_com/pelican-themes/bootstrap3/static/css/."
    os.system(cmd)
    cmd = "cp bower_components/font-awesome/fonts/* ../vurple_com/pelican-themes/bootstrap3/static/fonts/."
    os.system(cmd)

    cmd = "cp bower_components/bootstrap/fonts/* ../vurple_com/pelican-themes/bootstrap3/static/fonts/."
    os.system(cmd)
    cmd = "cp bower_components/bootstrap/dist/js/* ../vurple_com/pelican-themes/bootstrap3/static/js/."
    os.system(cmd)

if __name__ == '__main__':
    main()
