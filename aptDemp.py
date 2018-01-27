#!/usr/bin/python
# -*- coding: UTF-8 -*-


#created by yqbjtu on 2018/01/27
'''
fyi
https://apt.alioth.debian.org/python-apt-doc/library/index.html
https://apt.alioth.debian.org/python-apt-doc/library/apt_pkg.html
'''
import string
import sys
import apt
import apt_pkg


#this program will show how to install or query by python apt module

def checkPackage(pkgname):
    cache = apt.Cache()

    my_apt_pkg = cache[pkgname] #apt.package.Package object
    ll_pkg = cache._cache[pkgname]  # the low-level package object, apt_pkg.Package object

    #
    if ll_pkg.current_state !=  apt_pkg.CURSTATE_NOT_INSTALLED:
        #https://apt.alioth.debian.org/python-apt-doc/library/apt_pkg.html#curstates

        print "pkgName:" +  ll_pkg.get_fullname() +  ", version: " + ll_pkg.current_ver.ver_str + ",DescLang:"+ ll_pkg.current_ver.translated_description.language_code + ",State:%d" % (ll_pkg.current_state)
        print "this package info in Cache:"
        print ll_pkg.version_list 
    else:
        print "pkg:" +  pkgname +  " is not installed."


    if my_apt_pkg.is_installed:
        print "{pkg_name} already is installed".format(pkg_name=pkgname)
    else:
        my_apt_pkg.mark_install()

        try:
            cache.commit()
        except Exception, arg:
            print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))
    print "End."
    #end of checkPackage function

if len(sys.argv)==2:
    pkgname =  sys.argv[1]
    checkPackage(pkgname)
else:
    print "Usage:%s softwareName" % (sys.argv[0])







