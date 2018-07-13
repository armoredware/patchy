import urllib.request
import os, sys
import shutil
from shutil import copytree, ignore_patterns
import re
from PIL import Image
from io import BytesIO
import requests

#Global Variables
src_dirs = []
dst_dirs = []


#Settings
srvrs = ['web135',
#'web156',
#'web157'
]
subdomains = [
#'keepingsafe', 
'tlc',
'archives',
#Patched as test using pathyOneSite.py 'citizenparticipation',
#DO NOT PATCH HMRF 'environment',
'homes',
'correction',
'humanrights',
'publicworks',
'publicsafety',
'transportation',
'youth',
#'j3',
'africanamerican',
'airport',
'business',
'climatechange',
'consumer',
'disabled',
'doit',
'dpwt',
'emergencyservices',
'finance',
'golf',
'health',
'hispanic',
'humanresources',
'humanrights',
'labs',
'lgbt',
'mentalhealth',
'parksweb',
'planning',
'probation',
'seniorcitizens',
'socialservices',
'veterans',
'westchester2025',
'women',
'youth',
'bps',
'wtasc'
]


#Load Source Files

admin_dir = 'C:/inetpub/wwwroot/patchy/administrator/'
bin_dir = 'C:/inetpub/wwwroot/patchy/bin/'
cache_dir = 'C:/inetpub/wwwroot/patchy/cache/'
cli_dir = 'C:/inetpub/wwwroot/patchy/cli/'
comp_dir = 'C:/inetpub/wwwroot/patchy/components/'
incl_dir = 'C:/inetpub/wwwroot/patchy/includes/'
lang_dir = 'C:/inetpub/wwwroot/patchy/language/'
layout_dir = 'C:/inetpub/wwwroot/patchy/layouts/'
lib_dir = 'C:/inetpub/wwwroot/patchy/libraries/'
logs_dir = 'C:/inetpub/wwwroot/patchy/logs/'
media_dir = 'C:/inetpub/wwwroot/patchy/media/'
mod_dir = 'C:/inetpub/wwwroot/patchy/modules/'
plug_dir = 'C:/inetpub/wwwroot/patchy/plugins/'
templ_dir = 'C:/inetpub/wwwroot/patchy/templates/'
tmp_dir = 'C:/inetpub/wwwroot/patchy/tmp/'

#Iniatilize List for Source Directories
src_dirs.append(admin_dir)
src_dirs.append(bin_dir)
src_dirs.append(cache_dir)
src_dirs.append(cli_dir)
src_dirs.append(comp_dir)
src_dirs.append(incl_dir)
src_dirs.append(lang_dir)
src_dirs.append(layout_dir)
src_dirs.append(lib_dir)
src_dirs.append(logs_dir)
src_dirs.append(media_dir)
src_dirs.append(mod_dir)
src_dirs.append(plug_dir)
src_dirs.append(templ_dir)
src_dirs.append(tmp_dir)

#Destination
def set_dst_dirs(srvr, sudomain):
    admin_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/administrator'
    bin_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/bin'
    cache_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/cache'
    cli_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/cli'
    comp_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/components'
    incl_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/includes'
    lang_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/language'
    layout_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/layouts'
    lib_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/libraries'
    logs_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/logs'
    media_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/media'
    mod_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/modules'
    plug_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/plugins'
    templ_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/templates'
    tmp_dir_dst = '//'+srvr+'/c$/inetpub/wwwroot/'+subdomain+'/tmp'
    #Initialize Destination into List
    dst_dirs.insert(0, admin_dir_dst)
    dst_dirs.insert(1, bin_dir_dst)
    dst_dirs.insert(2, cache_dir_dst)
    dst_dirs.insert(3, cli_dir_dst)
    dst_dirs.insert(4, comp_dir_dst)
    dst_dirs.insert(5, incl_dir_dst)
    dst_dirs.insert(6, lang_dir_dst)
    dst_dirs.insert(7, layout_dir_dst)
    dst_dirs.insert(8, lib_dir_dst)
    dst_dirs.insert(9, logs_dir_dst)
    dst_dirs.insert(10, media_dir_dst)
    dst_dirs.insert(11, mod_dir_dst)
    dst_dirs.insert(12, plug_dir_dst)
    dst_dirs.insert(13, templ_dir_dst)
    dst_dirs.insert(14, tmp_dir_dst)


#while (os.path.isdir(src_dirs[0])):
'''if(os.path.isdir(src_dirs[0])):
    print ('removing : ', dst_dirs[0])
    shutil.rmtree(dst_dirs[0], ignore_errors=True)
print('copying : ', src_dirs[0])
shutil.copytree(src_dirs[0], dst_dirs[0], ignore = None)'''
#print (src_dirs[0])
#print (dst_dirs[0])

#Copy Necessary Directories

def apply_patch():
    incr = 0
    for x in src_dirs:
        #print('Copying From Source Dirs:', x)
        while (os.path.isdir(dst_dirs[incr])):
            print('Removing Dirs: ', dst_dirs[incr])
            try:
                shutil.rmtree(dst_dirs[incr], ignore_errors=True)
            except shutil.Error as e:
                print (str(e))
                #shutil.copytree(templ_src1, templ_dst1, ignore = ignore_patterns('*.html', '*.php', '*.db', 'tmp*'))
        print('Copy From:', x, ' to ', dst_dirs[incr])
        try:
            shutil.copytree(x, dst_dirs[incr], ignore = None)
        except shutil.Error as e:
            print (str(e))
        incr += 1


for srvr in srvrs:
    for subdomain in subdomains:
            print("Patching Files On : ", srvr)
            set_dst_dirs(srvr, subdomain)
            print("Patching Subdomain:", subdomain)
            apply_patch()
    