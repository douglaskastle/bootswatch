import re
import os

values = { 
#     'uc': 'Grissom',
    'lc': 'mutara',
    'header': 'Michroma',
    'body': 'Play',
    'website': 'mavek_org',
#     'cl': '#116BB7',
}


def main():
    
    src = 'cyborg'
    
    cmd = 'cp -r {0}/* {1}'.format(src, values['lc'])
    os.system(cmd)
    
    infile = "{0}/bootswatch.less".format(src)
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    outfile = values['lc'] + "/bootswatch.less"
    f = open(outfile, 'w')
    for line in lines:
        line = re.sub(src.title(), values['lc'].title(), line)
        if re.search("Roboto", line):
            continue
        if re.search("web-font-path", line):
            line = '@web-font-path2: "https://fonts.googleapis.com/css?family={0}:400,700,400italic";\n'.format(values['body']) + line
            line = '@web-font-path: "https://fonts.googleapis.com/css?family={0}:300italic,400italic,700italic,400,300,700";\n'.format(values['header']) + line
            line = line + '.web-font(@web-font-path2);\n'
        
        f.write(line)
    f.close()

    
    infile = "{0}/variables.less".format(src)
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    swap_list = {
        '@brand-primary:':                      '@brand-primary:         #00ff00',
        '@brand-success:':                      '@brand-success:         #0000ff',
        '@text-color:':                         '@text-color:            #ffffff',
        '@headings-color:':                     '@headings-color:          #00ff00',
        '@border-radius-base:':                 '@border-radius-base:        20px',
        '@border-radius-large:':                '@border-radius-large:       22px',
        '@border-radius-small:':                '@border-radius-small:       19px',
        '@component-active-color:':             '@component-active-color:    #00ff00',
        '@btn-default-color:':                  '@btn-default-color:              #000',
        '@btn-default-bg:':                     '@btn-default-bg:                 lighten(@gray-dark, 50%)',
        '@input-bg:':                           '@input-bg:                       @gray-dark',
        '@input-group-addon-bg:':               '@input-group-addon-bg:           @gray-lighter',
        '@dropdown-border:':                    '@dropdown-border:                rgba(0,255,0,0.1)',
        '@dropdown-divider-bg:':                '@dropdown-divider-bg:            rgba(0,255,0,0.1)',
        '@dropdown-link-color:':                '@dropdown-link-color:            #00ff00',
        '@dropdown-link-hover-color:':          '@dropdown-link-hover-color:      #00ff00',
        '@dropdown-link-active-color:':         '@dropdown-link-active-color:     #00ff00',
        '@navbar-default-link-hover-color:':    '@navbar-default-link-hover-color:          #00ff00',
        '@navbar-default-link-active-color:':   '@navbar-default-link-active-color:         #00ff00',
        '@navbar-default-brand-color:':         '@navbar-default-brand-color:               #00ff00',
        '@navbar-default-brand-hover-color:':   '@navbar-default-brand-hover-color:         #00ff00',
        '@navbar-inverse-link-hover-color:':    '@navbar-inverse-link-hover-color:           #0000ff',
        '@navbar-inverse-brand-color:':         '@navbar-inverse-brand-color:                #0000ff',
        '@navbar-inverse-brand-hover-color:':   '@navbar-inverse-brand-hover-color:          #0000ff',
        '@navbar-inverse-toggle-hover-bg:':     '@navbar-inverse-toggle-hover-bg:            #8080ff',
        '@navbar-inverse-toggle-icon-bar-bg:':  '@navbar-inverse-toggle-icon-bar-bg:         #0000ff',
        '@navbar-inverse-toggle-border-color:': '@navbar-inverse-toggle-border-color:        #8080ff',
        '@nav-tabs-active-link-hover-color:':   '@nav-tabs-active-link-hover-color:          #000',
        '@pagination-color:':                   '@pagination-color:                     #000',
        '@pagination-bg:':                      '@pagination-bg:                        @gray',
        '@pagination-hover-color:':             '@pagination-hover-color:               #000',
        '@pagination-active-color:':            '@pagination-active-color:              #000',
        '@pagination-disabled-bg:':             '@pagination-disabled-bg:               @gray',
        '@state-success-text:':                 '@state-success-text:             #000',
        '@state-info-text:':                    '@state-info-text:                #000',
        '@state-warning-text:':                 '@state-warning-text:             #000',
        '@state-danger-text:':                  '@state-danger-text:              #000',
        '@tooltip-bg:':                         '@tooltip-bg:                  #000',
        '@popover-bg:':                         '@popover-bg:                          lighten(@body-bg, 10%)',
        '@popover-fallback-border-color:':      '@popover-fallback-border-color:       #999',
        '@popover-arrow-outer-color:':          '@popover-arrow-outer-color:           fadein(@popover-border-color, 5%)',
        '@popover-arrow-outer-fallback-color:': '@popover-arrow-outer-fallback-color:  darken(@popover-fallback-border-color, 20%)',
        '@label-color:':                        '@label-color:                 #000',
        '@label-link-hover-color:':             '@label-link-hover-color:      #000',
        '@list-group-link-heading-color:':      '@list-group-link-heading-color: #000',
        '@panel-primary-text:':                 '@panel-primary-text:          #000',
        '@badge-color:':                        '@badge-color:                 #000',
        '@badge-link-hover-color:':             '@badge-link-hover-color:      #000',
        '@badge-active-bg:':                    '@badge-active-bg:             #000',
        '@breadcrumb-color:':                   '@breadcrumb-color:              #00ff00',
        '@carousel-control-color:':             '@carousel-control-color:                      #000',
#         '': '',
    }

    outfile = values['lc'] + "/variables.less"
    f = open(outfile, 'w')
    for line in lines:
        line = re.sub(src.title(), values['lc'].title(), line)
        line = re.sub(src, values['lc'], line)
        #line = re.sub('Roboto', 'Michroma', line)

        for s in swap_list.keys():
            if re.search(s, line):
                line = swap_list[s] + ";\n"
        line = re.sub('headings-font-family:    @font-family-base', 'headings-font-family:    @font-family-header-sans-serif', line)
        if re.search("Roboto", line):
            line = re.sub('Roboto', '{0}'.format(values['body']), line)
            line = '@font-family-header-sans-serif:  "{0}", "Helvetica Neue", Helvetica, Arial, sans-serif;\n'.format(values['header']) + line
        f.write(line)
    f.close()

    infile = "{0}/index.html".format(src)
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    outfile = values['lc'] + "/index.html"
    f = open(outfile, 'w')
    for line in lines:
        line = re.sub(src.title(), values['lc'].title(), line)
        line = re.sub(src, values['lc'], line)
        line = re.sub('UA-[0-9\-]+', '', line)
        if re.search('bootstrap.css" media="screen"', line):
            line = line + '    <link rel="stylesheet" href="./bootstrap_fixes.css" media="screen">\n'
        f.write(line)
    f.close()
    
    grunt = "/cygdrive/c/Users/keeshand/AppData/Roaming/npm/grunt"
    cmd = "{0} swatch:{1}".format(grunt, values['lc'])
    os.system(cmd)
    
    
    cmd = "cp {0}/bootstrap.min.css ../{1}/pelican-themes/bootstrap3/static/css/bootstrap.{0}.min.css".format(values['lc'], values['website'])
    os.system(cmd)
    cmd = "cp {0}/bootstrap_fixes.css ../{1}/pelican-themes/bootstrap3/static/css/bootstrap_fixes.{0}.css".format(values['lc'], values['website'])
    os.system(cmd)

if __name__ == '__main__':
    main()
