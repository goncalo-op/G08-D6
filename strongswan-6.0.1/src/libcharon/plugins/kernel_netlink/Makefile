# Makefile.in generated by automake 1.16.5 from Makefile.am.
# src/libcharon/plugins/kernel_netlink/Makefile.  Generated from Makefile.in by configure.

# Copyright (C) 1994-2021 Free Software Foundation, Inc.

# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.




am__is_gnu_make = { \
  if test -z '$(MAKELEVEL)'; then \
    false; \
  elif test -n '$(MAKE_HOST)'; then \
    true; \
  elif test -n '$(MAKE_VERSION)' && test -n '$(CURDIR)'; then \
    true; \
  else \
    false; \
  fi; \
}
am__make_running_with_option = \
  case $${target_option-} in \
      ?) ;; \
      *) echo "am__make_running_with_option: internal error: invalid" \
              "target option '$${target_option-}' specified" >&2; \
         exit 1;; \
  esac; \
  has_opt=no; \
  sane_makeflags=$$MAKEFLAGS; \
  if $(am__is_gnu_make); then \
    sane_makeflags=$$MFLAGS; \
  else \
    case $$MAKEFLAGS in \
      *\\[\ \	]*) \
        bs=\\; \
        sane_makeflags=`printf '%s\n' "$$MAKEFLAGS" \
          | sed "s/$$bs$$bs[$$bs $$bs	]*//g"`;; \
    esac; \
  fi; \
  skip_next=no; \
  strip_trailopt () \
  { \
    flg=`printf '%s\n' "$$flg" | sed "s/$$1.*$$//"`; \
  }; \
  for flg in $$sane_makeflags; do \
    test $$skip_next = yes && { skip_next=no; continue; }; \
    case $$flg in \
      *=*|--*) continue;; \
        -*I) strip_trailopt 'I'; skip_next=yes;; \
      -*I?*) strip_trailopt 'I';; \
        -*O) strip_trailopt 'O'; skip_next=yes;; \
      -*O?*) strip_trailopt 'O';; \
        -*l) strip_trailopt 'l'; skip_next=yes;; \
      -*l?*) strip_trailopt 'l';; \
      -[dEDm]) skip_next=yes;; \
      -[JT]) skip_next=yes;; \
    esac; \
    case $$flg in \
      *$$target_option*) has_opt=yes; break;; \
    esac; \
  done; \
  test $$has_opt = yes
am__make_dryrun = (target_option=n; $(am__make_running_with_option))
am__make_keepgoing = (target_option=k; $(am__make_running_with_option))
pkgdatadir = $(datadir)/strongswan
pkgincludedir = $(includedir)/strongswan
pkglibdir = $(libdir)/strongswan
pkglibexecdir = $(libexecdir)/strongswan
am__cd = CDPATH="$${ZSH_VERSION+.}$(PATH_SEPARATOR)" && cd
install_sh_DATA = $(install_sh) -c -m 644
install_sh_PROGRAM = $(install_sh) -c
install_sh_SCRIPT = $(install_sh) -c
INSTALL_HEADER = $(INSTALL_DATA)
transform = $(program_transform_name)
NORMAL_INSTALL = :
PRE_INSTALL = :
POST_INSTALL = :
NORMAL_UNINSTALL = :
PRE_UNINSTALL = :
POST_UNINSTALL = :
build_triplet = x86_64-pc-linux-gnu
host_triplet = x86_64-pc-linux-gnu
TESTS = kernel_netlink_tests$(EXEEXT)
check_PROGRAMS = $(am__EXEEXT_1)
subdir = src/libcharon/plugins/kernel_netlink
ACLOCAL_M4 = $(top_srcdir)/aclocal.m4
am__aclocal_m4_deps = $(top_srcdir)/m4/config/libtool.m4 \
	$(top_srcdir)/m4/config/ltoptions.m4 \
	$(top_srcdir)/m4/config/ltsugar.m4 \
	$(top_srcdir)/m4/config/ltversion.m4 \
	$(top_srcdir)/m4/config/lt~obsolete.m4 \
	$(top_srcdir)/m4/macros/split-package-version.m4 \
	$(top_srcdir)/m4/macros/with.m4 \
	$(top_srcdir)/m4/macros/enable-disable.m4 \
	$(top_srcdir)/m4/macros/add-plugin.m4 \
	$(top_srcdir)/configure.ac
am__configure_deps = $(am__aclocal_m4_deps) $(CONFIGURE_DEPENDENCIES) \
	$(ACLOCAL_M4)
DIST_COMMON = $(srcdir)/Makefile.am $(am__DIST_COMMON)
mkinstalldirs = $(install_sh) -d
CONFIG_HEADER = $(top_builddir)/config.h
CONFIG_CLEAN_FILES =
CONFIG_CLEAN_VPATH_FILES =
am__EXEEXT_1 = kernel_netlink_tests$(EXEEXT)
am__vpath_adj_setup = srcdirstrip=`echo "$(srcdir)" | sed 's|.|.|g'`;
am__vpath_adj = case $$p in \
    $(srcdir)/*) f=`echo "$$p" | sed "s|^$$srcdirstrip/||"`;; \
    *) f=$$p;; \
  esac;
am__strip_dir = f=`echo $$p | sed -e 's|^.*/||'`;
am__install_max = 40
am__nobase_strip_setup = \
  srcdirstrip=`echo "$(srcdir)" | sed 's/[].[^$$\\*|]/\\\\&/g'`
am__nobase_strip = \
  for p in $$list; do echo "$$p"; done | sed -e "s|$$srcdirstrip/||"
am__nobase_list = $(am__nobase_strip_setup); \
  for p in $$list; do echo "$$p $$p"; done | \
  sed "s| $$srcdirstrip/| |;"' / .*\//!s/ .*/ ./; s,\( .*\)/[^/]*$$,\1,' | \
  $(AWK) 'BEGIN { files["."] = "" } { files[$$2] = files[$$2] " " $$1; \
    if (++n[$$2] == $(am__install_max)) \
      { print $$2, files[$$2]; n[$$2] = 0; files[$$2] = "" } } \
    END { for (dir in files) print dir, files[dir] }'
am__base_list = \
  sed '$$!N;$$!N;$$!N;$$!N;$$!N;$$!N;$$!N;s/\n/ /g' | \
  sed '$$!N;$$!N;$$!N;$$!N;s/\n/ /g'
am__uninstall_files_from_dir = { \
  test -z "$$files" \
    || { test ! -d "$$dir" && test ! -f "$$dir" && test ! -r "$$dir"; } \
    || { echo " ( cd '$$dir' && rm -f" $$files ")"; \
         $(am__cd) "$$dir" && rm -f $$files; }; \
  }
am__installdirs = "$(DESTDIR)$(plugindir)"
LTLIBRARIES = $(noinst_LTLIBRARIES) $(plugin_LTLIBRARIES)
am__DEPENDENCIES_1 =
libstrongswan_kernel_netlink_la_DEPENDENCIES = $(am__DEPENDENCIES_1)
am_libstrongswan_kernel_netlink_la_OBJECTS = kernel_netlink_plugin.lo \
	kernel_netlink_ipsec.lo kernel_netlink_net.lo \
	kernel_netlink_shared.lo kernel_netlink_xfrmi.lo
libstrongswan_kernel_netlink_la_OBJECTS =  \
	$(am_libstrongswan_kernel_netlink_la_OBJECTS)
AM_V_lt = $(am__v_lt_$(V))
am__v_lt_ = $(am__v_lt_$(AM_DEFAULT_VERBOSITY))
am__v_lt_0 = --silent
am__v_lt_1 = 
libstrongswan_kernel_netlink_la_LINK = $(LIBTOOL) $(AM_V_lt) --tag=CC \
	$(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=link $(CCLD) \
	$(AM_CFLAGS) $(CFLAGS) \
	$(libstrongswan_kernel_netlink_la_LDFLAGS) $(LDFLAGS) -o $@
am_libstrongswan_kernel_netlink_la_rpath = -rpath \
	$(plugindir)
#am_libstrongswan_kernel_netlink_la_rpath =
am__dirstamp = $(am__leading_dot)dirstamp
am_kernel_netlink_tests_OBJECTS =  \
	kernel_netlink_tests-tests.$(OBJEXT) \
	suites/kernel_netlink_tests-test_socket.$(OBJEXT) \
	kernel_netlink_tests-kernel_netlink_shared.$(OBJEXT)
kernel_netlink_tests_OBJECTS = $(am_kernel_netlink_tests_OBJECTS)
kernel_netlink_tests_DEPENDENCIES =  \
	$(top_builddir)/src/libstrongswan/libstrongswan.la \
	$(top_builddir)/src/libstrongswan/tests/libtest.la
kernel_netlink_tests_LINK = $(LIBTOOL) $(AM_V_lt) --tag=CC \
	$(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=link $(CCLD) \
	$(kernel_netlink_tests_CFLAGS) $(CFLAGS) \
	$(kernel_netlink_tests_LDFLAGS) $(LDFLAGS) -o $@
AM_V_P = $(am__v_P_$(V))
am__v_P_ = $(am__v_P_$(AM_DEFAULT_VERBOSITY))
am__v_P_0 = false
am__v_P_1 = :
AM_V_GEN = $(am__v_GEN_$(V))
am__v_GEN_ = $(am__v_GEN_$(AM_DEFAULT_VERBOSITY))
am__v_GEN_0 = @echo "  GEN     " $@;
am__v_GEN_1 = 
AM_V_at = $(am__v_at_$(V))
am__v_at_ = $(am__v_at_$(AM_DEFAULT_VERBOSITY))
am__v_at_0 = @
am__v_at_1 = 
DEFAULT_INCLUDES = -I. -I$(top_builddir)
depcomp = $(SHELL) $(top_srcdir)/depcomp
am__maybe_remake_depfiles = depfiles
am__depfiles_remade = ./$(DEPDIR)/kernel_netlink_ipsec.Plo \
	./$(DEPDIR)/kernel_netlink_net.Plo \
	./$(DEPDIR)/kernel_netlink_plugin.Plo \
	./$(DEPDIR)/kernel_netlink_shared.Plo \
	./$(DEPDIR)/kernel_netlink_tests-kernel_netlink_shared.Po \
	./$(DEPDIR)/kernel_netlink_tests-tests.Po \
	./$(DEPDIR)/kernel_netlink_xfrmi.Plo \
	suites/$(DEPDIR)/kernel_netlink_tests-test_socket.Po
am__mv = mv -f
COMPILE = $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) \
	$(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS)
LTCOMPILE = $(LIBTOOL) $(AM_V_lt) --tag=CC $(AM_LIBTOOLFLAGS) \
	$(LIBTOOLFLAGS) --mode=compile $(CC) $(DEFS) \
	$(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) \
	$(AM_CFLAGS) $(CFLAGS)
AM_V_CC = $(am__v_CC_$(V))
am__v_CC_ = $(am__v_CC_$(AM_DEFAULT_VERBOSITY))
am__v_CC_0 = @echo "  CC      " $@;
am__v_CC_1 = 
CCLD = $(CC)
LINK = $(LIBTOOL) $(AM_V_lt) --tag=CC $(AM_LIBTOOLFLAGS) \
	$(LIBTOOLFLAGS) --mode=link $(CCLD) $(AM_CFLAGS) $(CFLAGS) \
	$(AM_LDFLAGS) $(LDFLAGS) -o $@
AM_V_CCLD = $(am__v_CCLD_$(V))
am__v_CCLD_ = $(am__v_CCLD_$(AM_DEFAULT_VERBOSITY))
am__v_CCLD_0 = @echo "  CCLD    " $@;
am__v_CCLD_1 = 
SOURCES = $(libstrongswan_kernel_netlink_la_SOURCES) \
	$(kernel_netlink_tests_SOURCES)
DIST_SOURCES = $(libstrongswan_kernel_netlink_la_SOURCES) \
	$(kernel_netlink_tests_SOURCES)
am__can_run_installinfo = \
  case $$AM_UPDATE_INFO_DIR in \
    n|no|NO) false;; \
    *) (install-info --version) >/dev/null 2>&1;; \
  esac
am__tagged_files = $(HEADERS) $(SOURCES) $(TAGS_FILES) $(LISP)
# Read a list of newline-separated strings from the standard input,
# and print each of them once, without duplicates.  Input order is
# *not* preserved.
am__uniquify_input = $(AWK) '\
  BEGIN { nonempty = 0; } \
  { items[$$0] = 1; nonempty = 1; } \
  END { if (nonempty) { for (i in items) print i; }; } \
'
# Make sure the list of sources is unique.  This is necessary because,
# e.g., the same source file might be shared among _SOURCES variables
# for different programs/libraries.
am__define_uniq_tagged_files = \
  list='$(am__tagged_files)'; \
  unique=`for i in $$list; do \
    if test -f "$$i"; then echo $$i; else echo $(srcdir)/$$i; fi; \
  done | $(am__uniquify_input)`
am__tty_colors_dummy = \
  mgn= red= grn= lgn= blu= brg= std=; \
  am__color_tests=no
am__tty_colors = { \
  $(am__tty_colors_dummy); \
  if test "X$(AM_COLOR_TESTS)" = Xno; then \
    am__color_tests=no; \
  elif test "X$(AM_COLOR_TESTS)" = Xalways; then \
    am__color_tests=yes; \
  elif test "X$$TERM" != Xdumb && { test -t 1; } 2>/dev/null; then \
    am__color_tests=yes; \
  fi; \
  if test $$am__color_tests = yes; then \
    red='[0;31m'; \
    grn='[0;32m'; \
    lgn='[1;32m'; \
    blu='[1;34m'; \
    mgn='[0;35m'; \
    brg='[1m'; \
    std='[m'; \
  fi; \
}
am__DIST_COMMON = $(srcdir)/Makefile.in $(top_srcdir)/depcomp
DISTFILES = $(DIST_COMMON) $(DIST_SOURCES) $(TEXINFOS) $(EXTRA_DIST)
ACLOCAL = ${SHELL} '/home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1/missing' aclocal-1.16
ALLOCA = 
AMTAR = $${TAR-tar}
AM_DEFAULT_VERBOSITY = 1
AR = ar
ATOMICLIB = 
AUTOCONF = ${SHELL} '/home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1/missing' autoconf
AUTOHEADER = ${SHELL} '/home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1/missing' autoheader
AUTOMAKE = ${SHELL} '/home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1/missing' automake-1.16
AWK = gawk
BFDLIB = 
BTLIB = 
CC = gcc
CCDEPMODE = depmode=gcc3
CFLAGS =  -Wno-format -Wno-format-security -Wno-implicit-fallthrough -Wno-missing-field-initializers -Wno-pointer-sign -Wno-sign-compare -Wno-type-limits -Wno-unused-parameter -g -O2 -include /home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1/config.h
COVERAGE_CFLAGS = 
COVERAGE_LDFLAGS = 
CPP = gcc -E
CPPFLAGS = 
CSCOPE = cscope
CTAGS = ctags
CYGPATH_W = echo
DEFS = -DHAVE_CONFIG_H
DEPDIR = .deps
DLLIB = 
DLLTOOL = false
DSYMUTIL = 
DUMPBIN = 
ECHO_C = 
ECHO_N = -n
ECHO_T = 
EGREP = /usr/bin/grep -E
ETAGS = etags
EXEEXT = 
FGREP = /usr/bin/grep -F
FILECMD = file
FUZZING_CFLAGS = 
FUZZING_LDFLAGS = 
GEM = 
GENHTML = 
GIT_VERSION = 6.0.1
GPERF = 
GPERF_LEN_TYPE = 
GPRBUILD = 
GREP = /usr/bin/grep
INSTALL = /usr/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644
INSTALL_PROGRAM = ${INSTALL}
INSTALL_SCRIPT = ${INSTALL}
INSTALL_STRIP_PROGRAM = $(install_sh) -c -s
LCOV = 
LD = /usr/bin/ld -m elf_x86_64
LDFLAGS = 
LEX = flex
LEXLIB = 
LEX_OUTPUT_ROOT = lex.yy
LIBOBJS = 
LIBS = 
LIBTOOL = $(SHELL) $(top_builddir)/libtool
LIPO = 
LN_S = ln -s
LSAN_OPTIONS = 
LTLIBOBJS = 
LT_SYS_LIBRARY_PATH = 
MAKEINFO = ${SHELL} '/home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1/missing' makeinfo
MANIFEST_TOOL = :
MKDIR_P = /usr/bin/mkdir -p
MYSQLCFLAG = 
MYSQLCONFIG = 
MYSQLLIB = 
NM = /usr/bin/nm -B
NMEDIT = 
OBJDUMP = objdump
OBJEXT = o
OPENSSL_LIB = -lcrypto
OTOOL = 
OTOOL64 = 
PACKAGE = strongswan
PACKAGE_BUGREPORT = 
PACKAGE_NAME = strongSwan
PACKAGE_STRING = strongSwan 6.0.1
PACKAGE_TARNAME = strongswan
PACKAGE_URL = 
PACKAGE_VERSION = 6.0.1
PACKAGE_VERSION_BUILD = 1
PACKAGE_VERSION_MAJOR = 6
PACKAGE_VERSION_MINOR = 0
PACKAGE_VERSION_REVIEW = 
PATH_SEPARATOR = :
PERL = /usr/bin/perl
PKG_CONFIG = /usr/bin/pkg-config
PKG_CONFIG_LIBDIR = 
PKG_CONFIG_PATH = 
PLUGIN_CFLAGS =  -rdynamic
PTHREADLIB = 
PYTHON = /usr/bin/python
PYTHON_EXEC_PREFIX = ${exec_prefix}
PYTHON_PACKAGE_VERSION = 
PYTHON_PLATFORM = linux
PYTHON_PREFIX = ${prefix}
PYTHON_VERSION = 3.13
PY_TEST = 
RANLIB = ranlib
RTLIB = 
RUBYGEMDIR = 
SED = /usr/bin/sed
SET_MAKE = 
SHELL = /bin/bash
SOCKLIB = 
STRIP = strip
TESTS_ENVIRONMENT = 
TOX = 
UNWINDLIB = 
VERSION = 6.0.1
YACC = yacc
YFLAGS = 
abs_builddir = /home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1/src/libcharon/plugins/kernel_netlink
abs_srcdir = /home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1/src/libcharon/plugins/kernel_netlink
abs_top_builddir = /home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1
abs_top_srcdir = /home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1
ac_ct_AR = ar
ac_ct_CC = gcc
ac_ct_DUMPBIN = 
aikgen_plugins =  mgf1 random nonce x509 pubkey pkcs1 pem openssl gmp
am__include = include
am__leading_dot = .
am__quote = 
am__tar = tar --format=ustar -chf - "$$tardir"
am__untar = tar -xf -
attest_plugins =  mgf1 random x509 pkcs1 pem openssl pkcs8 gmp
bindir = ${exec_prefix}/bin
botan_CFLAGS = 
botan_LIBS = 
build = x86_64-pc-linux-gnu
build_alias = 
build_cpu = x86_64
build_os = linux-gnu
build_vendor = pc
builddir = .
c_plugins =  attr kernel-netlink resolve socket-default vici updown xauth-generic counters
charon_natt_port = 4500
charon_plugins =  mgf1 random nonce x509 revocation constraints pubkey pkcs1 pkcs7 pgp dnskey sshkey pem openssl pkcs8 gmp xcbc cmac kdf drbg curl attr kernel-netlink resolve socket-default vici updown xauth-generic counters
charon_udp_port = 500
clearsilver_LIBS = 
cmd_plugins =  mgf1 random nonce x509 revocation constraints pubkey pkcs1 pkcs7 sshkey pem openssl pkcs8 gmp xcbc cmac kdf drbg curl kernel-netlink resolve socket-default xauth-generic
datadir = ${datarootdir}
datarootdir = ${prefix}/share
dbusdatadir = ${prefix}/share
dbuspolicydir = ${prefix}/share/dbus-1/system.d
dev_headers = no
docdir = ${datarootdir}/doc/${PACKAGE_TARNAME}
dvidir = ${docdir}
exec_prefix = ${prefix}
fips_mode = 0
fuzz_plugins =  x509 pkcs1 pem gmp
host = x86_64-pc-linux-gnu
host_alias = 
host_cpu = x86_64
host_os = linux-gnu
host_vendor = pc
htmldir = ${docdir}
imcvdir = ${exec_prefix}/lib/ipsec/imcvs
includedir = ${prefix}/include
infodir = ${datarootdir}/info
install_sh = ${SHELL} /home/salithekid/Desktop/Projeto3Cadeiras/strongswan-6.0.1/install-sh
ipsec_script = ipsec
ipsec_script_upper = IPSEC
ipsecdir = ${exec_prefix}/libexec/ipsec
ipsecgroup = root
ipseclibdir = ${exec_prefix}/lib/ipsec
ipsecuser = root
json_CFLAGS = 
json_LIBS = 
libdir = ${exec_prefix}/lib
libexecdir = ${exec_prefix}/libexec
libfuzzer = 
libiptc_CFLAGS = 
libiptc_LIBS = 
linux_headers = ${top_srcdir}/src/include
localedir = ${datarootdir}/locale
localstatedir = ${prefix}/var
manager_plugins =  random pkcs1 pem openssl pkcs8 gmp
mandir = ${datarootdir}/man
medsrv_plugins =  mgf1 random pkcs1 pem openssl pkcs8 gmp
mkdir_p = $(MKDIR_P)
nm_CFLAGS = 
nm_LIBS = 
nm_ca_dir = /usr/share/ca-certificates
nm_plugins =  mgf1 random nonce x509 revocation constraints pkcs1 pkcs7 sshkey pem openssl pkcs8 gmp xcbc cmac kdf drbg curl kernel-netlink socket-default
oldincludedir = /usr/include
p_plugins = 
pcsclite_CFLAGS = 
pcsclite_LIBS = 
pdfdir = ${docdir}
piddir = /var/run
pkgpyexecdir = ${pyexecdir}/strongswan
pkgpythondir = ${pythondir}/strongswan
pki_plugins =  mgf1 random x509 revocation constraints pubkey pkcs1 pkcs7 dnskey sshkey pem openssl pkcs8 gmp kdf drbg curl
plugindir = ${exec_prefix}/lib/ipsec/plugins
pool_plugins = 
prefix = /usr
program_transform_name = s,x,x,
psdir = ${docdir}
pyexecdir = ${PYTHON_EXEC_PREFIX}/lib/python3.13/site-packages
pythondir = ${PYTHON_PREFIX}/lib/python3.13/site-packages
random_device = /dev/random
resolv_conf = /etc/resolv.conf
routing_table = 220
routing_table_prio = 220
runstatedir = ${localstatedir}/run
s_plugins =  mgf1 random nonce x509 revocation constraints pubkey pkcs1 pkcs7 pgp dnskey sshkey pem openssl pkcs8 gmp xcbc cmac kdf drbg curl
sbindir = ${exec_prefix}/sbin
scripts_plugins =  mgf1 random x509 pkcs1 pkcs7 pem openssl pkcs8 gmp kdf drbg curl
selinux_CFLAGS = 
selinux_LIBS = 
sharedstatedir = ${prefix}/com
soup_CFLAGS = 
soup_LIBS = 
srcdir = .
strongswan_conf = /etc/strongswan.conf
strongswan_options =  charon charon-logging pki swanctl
swanctldir = /etc/swanctl
sysconfdir = /etc
systemd_CFLAGS = 
systemd_LIBS = 
systemd_daemon_CFLAGS = 
systemd_daemon_LIBS = 
systemd_journal_CFLAGS = 
systemd_journal_LIBS = 
systemdsystemunitdir = 
t_plugins = 
target_alias = 
top_build_prefix = ../../../../
top_builddir = ../../../..
top_srcdir = ../../../..
tss2_CFLAGS = 
tss2_LIBS = 
tss2_esys_CFLAGS = 
tss2_esys_LIBS = 
tss2_socket_CFLAGS = 
tss2_socket_LIBS = 
tss2_sys_CFLAGS = 
tss2_sys_LIBS = 
tss2_tabrmd_CFLAGS = 
tss2_tabrmd_LIBS = 
urandom_device = /dev/urandom
wolfssl_CFLAGS = 
wolfssl_LIBS = 
xml_CFLAGS = 
xml_LIBS = 
AM_CPPFLAGS = \
	-I${linux_headers} \
	-I$(top_srcdir)/src/libstrongswan \
	-I$(top_srcdir)/src/libcharon \
	-DROUTING_TABLE=${routing_table} \
	-DROUTING_TABLE_PRIO=${routing_table_prio}

AM_CFLAGS = \
	$(PLUGIN_CFLAGS)

#noinst_LTLIBRARIES = libstrongswan-kernel-netlink.la
plugin_LTLIBRARIES = libstrongswan-kernel-netlink.la
libstrongswan_kernel_netlink_la_SOURCES = \
	kernel_netlink_plugin.h kernel_netlink_plugin.c \
	kernel_netlink_ipsec.h kernel_netlink_ipsec.c \
	kernel_netlink_net.h kernel_netlink_net.c \
	kernel_netlink_shared.h kernel_netlink_shared.c \
	kernel_netlink_xfrmi.h kernel_netlink_xfrmi.c

libstrongswan_kernel_netlink_la_LIBADD = $(DLLIB)
libstrongswan_kernel_netlink_la_LDFLAGS = -module -avoid-version
kernel_netlink_tests_SOURCES = \
	tests.h tests.c \
	suites/test_socket.c \
	kernel_netlink_shared.c

kernel_netlink_tests_CFLAGS = \
	-I$(top_srcdir)/src/libstrongswan \
	-I$(top_srcdir)/src/libstrongswan/tests \
	-DNETLINK_MSG_LOSS_HOOK=netlink_msg_loss \
	

kernel_netlink_tests_LDFLAGS = 
kernel_netlink_tests_LDADD = \
	$(top_builddir)/src/libstrongswan/libstrongswan.la \
	$(top_builddir)/src/libstrongswan/tests/libtest.la

all: all-am

.SUFFIXES:
.SUFFIXES: .c .lo .o .obj
$(srcdir)/Makefile.in:  $(srcdir)/Makefile.am  $(am__configure_deps)
	@for dep in $?; do \
	  case '$(am__configure_deps)' in \
	    *$$dep*) \
	      ( cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh ) \
	        && { if test -f $@; then exit 0; else break; fi; }; \
	      exit 1;; \
	  esac; \
	done; \
	echo ' cd $(top_srcdir) && $(AUTOMAKE) --gnu src/libcharon/plugins/kernel_netlink/Makefile'; \
	$(am__cd) $(top_srcdir) && \
	  $(AUTOMAKE) --gnu src/libcharon/plugins/kernel_netlink/Makefile
Makefile: $(srcdir)/Makefile.in $(top_builddir)/config.status
	@case '$?' in \
	  *config.status*) \
	    cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh;; \
	  *) \
	    echo ' cd $(top_builddir) && $(SHELL) ./config.status $(subdir)/$@ $(am__maybe_remake_depfiles)'; \
	    cd $(top_builddir) && $(SHELL) ./config.status $(subdir)/$@ $(am__maybe_remake_depfiles);; \
	esac;

$(top_builddir)/config.status: $(top_srcdir)/configure $(CONFIG_STATUS_DEPENDENCIES)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh

$(top_srcdir)/configure:  $(am__configure_deps)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh
$(ACLOCAL_M4):  $(am__aclocal_m4_deps)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh
$(am__aclocal_m4_deps):

clean-checkPROGRAMS:
	@list='$(check_PROGRAMS)'; test -n "$$list" || exit 0; \
	echo " rm -f" $$list; \
	rm -f $$list || exit $$?; \
	test -n "$(EXEEXT)" || exit 0; \
	list=`for p in $$list; do echo "$$p"; done | sed 's/$(EXEEXT)$$//'`; \
	echo " rm -f" $$list; \
	rm -f $$list

clean-noinstLTLIBRARIES:
	-test -z "$(noinst_LTLIBRARIES)" || rm -f $(noinst_LTLIBRARIES)
	@list='$(noinst_LTLIBRARIES)'; \
	locs=`for p in $$list; do echo $$p; done | \
	      sed 's|^[^/]*$$|.|; s|/[^/]*$$||; s|$$|/so_locations|' | \
	      sort -u`; \
	test -z "$$locs" || { \
	  echo rm -f $${locs}; \
	  rm -f $${locs}; \
	}

install-pluginLTLIBRARIES: $(plugin_LTLIBRARIES)
	@$(NORMAL_INSTALL)
	@list='$(plugin_LTLIBRARIES)'; test -n "$(plugindir)" || list=; \
	list2=; for p in $$list; do \
	  if test -f $$p; then \
	    list2="$$list2 $$p"; \
	  else :; fi; \
	done; \
	test -z "$$list2" || { \
	  echo " $(MKDIR_P) '$(DESTDIR)$(plugindir)'"; \
	  $(MKDIR_P) "$(DESTDIR)$(plugindir)" || exit 1; \
	  echo " $(LIBTOOL) $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=install $(INSTALL) $(INSTALL_STRIP_FLAG) $$list2 '$(DESTDIR)$(plugindir)'"; \
	  $(LIBTOOL) $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=install $(INSTALL) $(INSTALL_STRIP_FLAG) $$list2 "$(DESTDIR)$(plugindir)"; \
	}

uninstall-pluginLTLIBRARIES:
	@$(NORMAL_UNINSTALL)
	@list='$(plugin_LTLIBRARIES)'; test -n "$(plugindir)" || list=; \
	for p in $$list; do \
	  $(am__strip_dir) \
	  echo " $(LIBTOOL) $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=uninstall rm -f '$(DESTDIR)$(plugindir)/$$f'"; \
	  $(LIBTOOL) $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=uninstall rm -f "$(DESTDIR)$(plugindir)/$$f"; \
	done

clean-pluginLTLIBRARIES:
	-test -z "$(plugin_LTLIBRARIES)" || rm -f $(plugin_LTLIBRARIES)
	@list='$(plugin_LTLIBRARIES)'; \
	locs=`for p in $$list; do echo $$p; done | \
	      sed 's|^[^/]*$$|.|; s|/[^/]*$$||; s|$$|/so_locations|' | \
	      sort -u`; \
	test -z "$$locs" || { \
	  echo rm -f $${locs}; \
	  rm -f $${locs}; \
	}

libstrongswan-kernel-netlink.la: $(libstrongswan_kernel_netlink_la_OBJECTS) $(libstrongswan_kernel_netlink_la_DEPENDENCIES) $(EXTRA_libstrongswan_kernel_netlink_la_DEPENDENCIES) 
	$(AM_V_CCLD)$(libstrongswan_kernel_netlink_la_LINK) $(am_libstrongswan_kernel_netlink_la_rpath) $(libstrongswan_kernel_netlink_la_OBJECTS) $(libstrongswan_kernel_netlink_la_LIBADD) $(LIBS)
suites/$(am__dirstamp):
	@$(MKDIR_P) suites
	@: > suites/$(am__dirstamp)
suites/$(DEPDIR)/$(am__dirstamp):
	@$(MKDIR_P) suites/$(DEPDIR)
	@: > suites/$(DEPDIR)/$(am__dirstamp)
suites/kernel_netlink_tests-test_socket.$(OBJEXT):  \
	suites/$(am__dirstamp) suites/$(DEPDIR)/$(am__dirstamp)

kernel_netlink_tests$(EXEEXT): $(kernel_netlink_tests_OBJECTS) $(kernel_netlink_tests_DEPENDENCIES) $(EXTRA_kernel_netlink_tests_DEPENDENCIES) 
	@rm -f kernel_netlink_tests$(EXEEXT)
	$(AM_V_CCLD)$(kernel_netlink_tests_LINK) $(kernel_netlink_tests_OBJECTS) $(kernel_netlink_tests_LDADD) $(LIBS)

mostlyclean-compile:
	-rm -f *.$(OBJEXT)
	-rm -f suites/*.$(OBJEXT)

distclean-compile:
	-rm -f *.tab.c

include ./$(DEPDIR)/kernel_netlink_ipsec.Plo # am--include-marker
include ./$(DEPDIR)/kernel_netlink_net.Plo # am--include-marker
include ./$(DEPDIR)/kernel_netlink_plugin.Plo # am--include-marker
include ./$(DEPDIR)/kernel_netlink_shared.Plo # am--include-marker
include ./$(DEPDIR)/kernel_netlink_tests-kernel_netlink_shared.Po # am--include-marker
include ./$(DEPDIR)/kernel_netlink_tests-tests.Po # am--include-marker
include ./$(DEPDIR)/kernel_netlink_xfrmi.Plo # am--include-marker
include suites/$(DEPDIR)/kernel_netlink_tests-test_socket.Po # am--include-marker

$(am__depfiles_remade):
	@$(MKDIR_P) $(@D)
	@echo '# dummy' >$@-t && $(am__mv) $@-t $@

am--depfiles: $(am__depfiles_remade)

.c.o:
	$(AM_V_CC)depbase=`echo $@ | sed 's|[^/]*$$|$(DEPDIR)/&|;s|\.o$$||'`;\
	$(COMPILE) -MT $@ -MD -MP -MF $$depbase.Tpo -c -o $@ $< &&\
	$(am__mv) $$depbase.Tpo $$depbase.Po
#	$(AM_V_CC)source='$<' object='$@' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(AM_V_CC_no)$(COMPILE) -c -o $@ $<

.c.obj:
	$(AM_V_CC)depbase=`echo $@ | sed 's|[^/]*$$|$(DEPDIR)/&|;s|\.obj$$||'`;\
	$(COMPILE) -MT $@ -MD -MP -MF $$depbase.Tpo -c -o $@ `$(CYGPATH_W) '$<'` &&\
	$(am__mv) $$depbase.Tpo $$depbase.Po
#	$(AM_V_CC)source='$<' object='$@' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(AM_V_CC_no)$(COMPILE) -c -o $@ `$(CYGPATH_W) '$<'`

.c.lo:
	$(AM_V_CC)depbase=`echo $@ | sed 's|[^/]*$$|$(DEPDIR)/&|;s|\.lo$$||'`;\
	$(LTCOMPILE) -MT $@ -MD -MP -MF $$depbase.Tpo -c -o $@ $< &&\
	$(am__mv) $$depbase.Tpo $$depbase.Plo
#	$(AM_V_CC)source='$<' object='$@' libtool=yes \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(AM_V_CC_no)$(LTCOMPILE) -c -o $@ $<

kernel_netlink_tests-tests.o: tests.c
	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -MT kernel_netlink_tests-tests.o -MD -MP -MF $(DEPDIR)/kernel_netlink_tests-tests.Tpo -c -o kernel_netlink_tests-tests.o `test -f 'tests.c' || echo '$(srcdir)/'`tests.c
	$(AM_V_at)$(am__mv) $(DEPDIR)/kernel_netlink_tests-tests.Tpo $(DEPDIR)/kernel_netlink_tests-tests.Po
#	$(AM_V_CC)source='tests.c' object='kernel_netlink_tests-tests.o' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(AM_V_CC_no)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -c -o kernel_netlink_tests-tests.o `test -f 'tests.c' || echo '$(srcdir)/'`tests.c

kernel_netlink_tests-tests.obj: tests.c
	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -MT kernel_netlink_tests-tests.obj -MD -MP -MF $(DEPDIR)/kernel_netlink_tests-tests.Tpo -c -o kernel_netlink_tests-tests.obj `if test -f 'tests.c'; then $(CYGPATH_W) 'tests.c'; else $(CYGPATH_W) '$(srcdir)/tests.c'; fi`
	$(AM_V_at)$(am__mv) $(DEPDIR)/kernel_netlink_tests-tests.Tpo $(DEPDIR)/kernel_netlink_tests-tests.Po
#	$(AM_V_CC)source='tests.c' object='kernel_netlink_tests-tests.obj' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(AM_V_CC_no)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -c -o kernel_netlink_tests-tests.obj `if test -f 'tests.c'; then $(CYGPATH_W) 'tests.c'; else $(CYGPATH_W) '$(srcdir)/tests.c'; fi`

suites/kernel_netlink_tests-test_socket.o: suites/test_socket.c
	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -MT suites/kernel_netlink_tests-test_socket.o -MD -MP -MF suites/$(DEPDIR)/kernel_netlink_tests-test_socket.Tpo -c -o suites/kernel_netlink_tests-test_socket.o `test -f 'suites/test_socket.c' || echo '$(srcdir)/'`suites/test_socket.c
	$(AM_V_at)$(am__mv) suites/$(DEPDIR)/kernel_netlink_tests-test_socket.Tpo suites/$(DEPDIR)/kernel_netlink_tests-test_socket.Po
#	$(AM_V_CC)source='suites/test_socket.c' object='suites/kernel_netlink_tests-test_socket.o' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(AM_V_CC_no)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -c -o suites/kernel_netlink_tests-test_socket.o `test -f 'suites/test_socket.c' || echo '$(srcdir)/'`suites/test_socket.c

suites/kernel_netlink_tests-test_socket.obj: suites/test_socket.c
	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -MT suites/kernel_netlink_tests-test_socket.obj -MD -MP -MF suites/$(DEPDIR)/kernel_netlink_tests-test_socket.Tpo -c -o suites/kernel_netlink_tests-test_socket.obj `if test -f 'suites/test_socket.c'; then $(CYGPATH_W) 'suites/test_socket.c'; else $(CYGPATH_W) '$(srcdir)/suites/test_socket.c'; fi`
	$(AM_V_at)$(am__mv) suites/$(DEPDIR)/kernel_netlink_tests-test_socket.Tpo suites/$(DEPDIR)/kernel_netlink_tests-test_socket.Po
#	$(AM_V_CC)source='suites/test_socket.c' object='suites/kernel_netlink_tests-test_socket.obj' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(AM_V_CC_no)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -c -o suites/kernel_netlink_tests-test_socket.obj `if test -f 'suites/test_socket.c'; then $(CYGPATH_W) 'suites/test_socket.c'; else $(CYGPATH_W) '$(srcdir)/suites/test_socket.c'; fi`

kernel_netlink_tests-kernel_netlink_shared.o: kernel_netlink_shared.c
	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -MT kernel_netlink_tests-kernel_netlink_shared.o -MD -MP -MF $(DEPDIR)/kernel_netlink_tests-kernel_netlink_shared.Tpo -c -o kernel_netlink_tests-kernel_netlink_shared.o `test -f 'kernel_netlink_shared.c' || echo '$(srcdir)/'`kernel_netlink_shared.c
	$(AM_V_at)$(am__mv) $(DEPDIR)/kernel_netlink_tests-kernel_netlink_shared.Tpo $(DEPDIR)/kernel_netlink_tests-kernel_netlink_shared.Po
#	$(AM_V_CC)source='kernel_netlink_shared.c' object='kernel_netlink_tests-kernel_netlink_shared.o' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(AM_V_CC_no)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -c -o kernel_netlink_tests-kernel_netlink_shared.o `test -f 'kernel_netlink_shared.c' || echo '$(srcdir)/'`kernel_netlink_shared.c

kernel_netlink_tests-kernel_netlink_shared.obj: kernel_netlink_shared.c
	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -MT kernel_netlink_tests-kernel_netlink_shared.obj -MD -MP -MF $(DEPDIR)/kernel_netlink_tests-kernel_netlink_shared.Tpo -c -o kernel_netlink_tests-kernel_netlink_shared.obj `if test -f 'kernel_netlink_shared.c'; then $(CYGPATH_W) 'kernel_netlink_shared.c'; else $(CYGPATH_W) '$(srcdir)/kernel_netlink_shared.c'; fi`
	$(AM_V_at)$(am__mv) $(DEPDIR)/kernel_netlink_tests-kernel_netlink_shared.Tpo $(DEPDIR)/kernel_netlink_tests-kernel_netlink_shared.Po
#	$(AM_V_CC)source='kernel_netlink_shared.c' object='kernel_netlink_tests-kernel_netlink_shared.obj' libtool=no \
#	DEPDIR=$(DEPDIR) $(CCDEPMODE) $(depcomp) \
#	$(AM_V_CC_no)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(kernel_netlink_tests_CFLAGS) $(CFLAGS) -c -o kernel_netlink_tests-kernel_netlink_shared.obj `if test -f 'kernel_netlink_shared.c'; then $(CYGPATH_W) 'kernel_netlink_shared.c'; else $(CYGPATH_W) '$(srcdir)/kernel_netlink_shared.c'; fi`

mostlyclean-libtool:
	-rm -f *.lo

clean-libtool:
	-rm -rf .libs _libs

ID: $(am__tagged_files)
	$(am__define_uniq_tagged_files); mkid -fID $$unique
tags: tags-am
TAGS: tags

tags-am: $(TAGS_DEPENDENCIES) $(am__tagged_files)
	set x; \
	here=`pwd`; \
	$(am__define_uniq_tagged_files); \
	shift; \
	if test -z "$(ETAGS_ARGS)$$*$$unique"; then :; else \
	  test -n "$$unique" || unique=$$empty_fix; \
	  if test $$# -gt 0; then \
	    $(ETAGS) $(ETAGSFLAGS) $(AM_ETAGSFLAGS) $(ETAGS_ARGS) \
	      "$$@" $$unique; \
	  else \
	    $(ETAGS) $(ETAGSFLAGS) $(AM_ETAGSFLAGS) $(ETAGS_ARGS) \
	      $$unique; \
	  fi; \
	fi
ctags: ctags-am

CTAGS: ctags
ctags-am: $(TAGS_DEPENDENCIES) $(am__tagged_files)
	$(am__define_uniq_tagged_files); \
	test -z "$(CTAGS_ARGS)$$unique" \
	  || $(CTAGS) $(CTAGSFLAGS) $(AM_CTAGSFLAGS) $(CTAGS_ARGS) \
	     $$unique

GTAGS:
	here=`$(am__cd) $(top_builddir) && pwd` \
	  && $(am__cd) $(top_srcdir) \
	  && gtags -i $(GTAGS_ARGS) "$$here"
cscopelist: cscopelist-am

cscopelist-am: $(am__tagged_files)
	list='$(am__tagged_files)'; \
	case "$(srcdir)" in \
	  [\\/]* | ?:[\\/]*) sdir="$(srcdir)" ;; \
	  *) sdir=$(subdir)/$(srcdir) ;; \
	esac; \
	for i in $$list; do \
	  if test -f "$$i"; then \
	    echo "$(subdir)/$$i"; \
	  else \
	    echo "$$sdir/$$i"; \
	  fi; \
	done >> $(top_builddir)/cscope.files

distclean-tags:
	-rm -f TAGS ID GTAGS GRTAGS GSYMS GPATH tags

check-TESTS: $(TESTS)
	@failed=0; all=0; xfail=0; xpass=0; skip=0; \
	srcdir=$(srcdir); export srcdir; \
	list=' $(TESTS) '; \
	$(am__tty_colors); \
	if test -n "$$list"; then \
	  for tst in $$list; do \
	    if test -f ./$$tst; then dir=./; \
	    elif test -f $$tst; then dir=; \
	    else dir="$(srcdir)/"; fi; \
	    if $(TESTS_ENVIRONMENT) $${dir}$$tst $(AM_TESTS_FD_REDIRECT); then \
	      all=`expr $$all + 1`; \
	      case " $(XFAIL_TESTS) " in \
	      *[\ \	]$$tst[\ \	]*) \
		xpass=`expr $$xpass + 1`; \
		failed=`expr $$failed + 1`; \
		col=$$red; res=XPASS; \
	      ;; \
	      *) \
		col=$$grn; res=PASS; \
	      ;; \
	      esac; \
	    elif test $$? -ne 77; then \
	      all=`expr $$all + 1`; \
	      case " $(XFAIL_TESTS) " in \
	      *[\ \	]$$tst[\ \	]*) \
		xfail=`expr $$xfail + 1`; \
		col=$$lgn; res=XFAIL; \
	      ;; \
	      *) \
		failed=`expr $$failed + 1`; \
		col=$$red; res=FAIL; \
	      ;; \
	      esac; \
	    else \
	      skip=`expr $$skip + 1`; \
	      col=$$blu; res=SKIP; \
	    fi; \
	    echo "$${col}$$res$${std}: $$tst"; \
	  done; \
	  if test "$$all" -eq 1; then \
	    tests="test"; \
	    All=""; \
	  else \
	    tests="tests"; \
	    All="All "; \
	  fi; \
	  if test "$$failed" -eq 0; then \
	    if test "$$xfail" -eq 0; then \
	      banner="$$All$$all $$tests passed"; \
	    else \
	      if test "$$xfail" -eq 1; then failures=failure; else failures=failures; fi; \
	      banner="$$All$$all $$tests behaved as expected ($$xfail expected $$failures)"; \
	    fi; \
	  else \
	    if test "$$xpass" -eq 0; then \
	      banner="$$failed of $$all $$tests failed"; \
	    else \
	      if test "$$xpass" -eq 1; then passes=pass; else passes=passes; fi; \
	      banner="$$failed of $$all $$tests did not behave as expected ($$xpass unexpected $$passes)"; \
	    fi; \
	  fi; \
	  dashes="$$banner"; \
	  skipped=""; \
	  if test "$$skip" -ne 0; then \
	    if test "$$skip" -eq 1; then \
	      skipped="($$skip test was not run)"; \
	    else \
	      skipped="($$skip tests were not run)"; \
	    fi; \
	    test `echo "$$skipped" | wc -c` -le `echo "$$banner" | wc -c` || \
	      dashes="$$skipped"; \
	  fi; \
	  report=""; \
	  if test "$$failed" -ne 0 && test -n "$(PACKAGE_BUGREPORT)"; then \
	    report="Please report to $(PACKAGE_BUGREPORT)"; \
	    test `echo "$$report" | wc -c` -le `echo "$$banner" | wc -c` || \
	      dashes="$$report"; \
	  fi; \
	  dashes=`echo "$$dashes" | sed s/./=/g`; \
	  if test "$$failed" -eq 0; then \
	    col="$$grn"; \
	  else \
	    col="$$red"; \
	  fi; \
	  echo "$${col}$$dashes$${std}"; \
	  echo "$${col}$$banner$${std}"; \
	  test -z "$$skipped" || echo "$${col}$$skipped$${std}"; \
	  test -z "$$report" || echo "$${col}$$report$${std}"; \
	  echo "$${col}$$dashes$${std}"; \
	  test "$$failed" -eq 0; \
	else :; fi
distdir: $(BUILT_SOURCES)
	$(MAKE) $(AM_MAKEFLAGS) distdir-am

distdir-am: $(DISTFILES)
	@srcdirstrip=`echo "$(srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	topsrcdirstrip=`echo "$(top_srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	list='$(DISTFILES)'; \
	  dist_files=`for file in $$list; do echo $$file; done | \
	  sed -e "s|^$$srcdirstrip/||;t" \
	      -e "s|^$$topsrcdirstrip/|$(top_builddir)/|;t"`; \
	case $$dist_files in \
	  */*) $(MKDIR_P) `echo "$$dist_files" | \
			   sed '/\//!d;s|^|$(distdir)/|;s,/[^/]*$$,,' | \
			   sort -u` ;; \
	esac; \
	for file in $$dist_files; do \
	  if test -f $$file || test -d $$file; then d=.; else d=$(srcdir); fi; \
	  if test -d $$d/$$file; then \
	    dir=`echo "/$$file" | sed -e 's,/[^/]*$$,,'`; \
	    if test -d "$(distdir)/$$file"; then \
	      find "$(distdir)/$$file" -type d ! -perm -700 -exec chmod u+rwx {} \;; \
	    fi; \
	    if test -d $(srcdir)/$$file && test $$d != $(srcdir); then \
	      cp -fpR $(srcdir)/$$file "$(distdir)$$dir" || exit 1; \
	      find "$(distdir)/$$file" -type d ! -perm -700 -exec chmod u+rwx {} \;; \
	    fi; \
	    cp -fpR $$d/$$file "$(distdir)$$dir" || exit 1; \
	  else \
	    test -f "$(distdir)/$$file" \
	    || cp -p $$d/$$file "$(distdir)/$$file" \
	    || exit 1; \
	  fi; \
	done
check-am: all-am
	$(MAKE) $(AM_MAKEFLAGS) $(check_PROGRAMS)
	$(MAKE) $(AM_MAKEFLAGS) check-TESTS
check: check-am
all-am: Makefile $(LTLIBRARIES)
installdirs:
	for dir in "$(DESTDIR)$(plugindir)"; do \
	  test -z "$$dir" || $(MKDIR_P) "$$dir"; \
	done
install: install-am
install-exec: install-exec-am
install-data: install-data-am
uninstall: uninstall-am

install-am: all-am
	@$(MAKE) $(AM_MAKEFLAGS) install-exec-am install-data-am

installcheck: installcheck-am
install-strip:
	if test -z '$(STRIP)'; then \
	  $(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	    install_sh_PROGRAM="$(INSTALL_STRIP_PROGRAM)" INSTALL_STRIP_FLAG=-s \
	      install; \
	else \
	  $(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	    install_sh_PROGRAM="$(INSTALL_STRIP_PROGRAM)" INSTALL_STRIP_FLAG=-s \
	    "INSTALL_PROGRAM_ENV=STRIPPROG='$(STRIP)'" install; \
	fi
mostlyclean-generic:

clean-generic:

distclean-generic:
	-test -z "$(CONFIG_CLEAN_FILES)" || rm -f $(CONFIG_CLEAN_FILES)
	-test . = "$(srcdir)" || test -z "$(CONFIG_CLEAN_VPATH_FILES)" || rm -f $(CONFIG_CLEAN_VPATH_FILES)
	-rm -f suites/$(DEPDIR)/$(am__dirstamp)
	-rm -f suites/$(am__dirstamp)

maintainer-clean-generic:
	@echo "This command is intended for maintainers to use"
	@echo "it deletes files that may require special tools to rebuild."
clean: clean-am

clean-am: clean-checkPROGRAMS clean-generic clean-libtool \
	clean-noinstLTLIBRARIES clean-pluginLTLIBRARIES mostlyclean-am

distclean: distclean-am
		-rm -f ./$(DEPDIR)/kernel_netlink_ipsec.Plo
	-rm -f ./$(DEPDIR)/kernel_netlink_net.Plo
	-rm -f ./$(DEPDIR)/kernel_netlink_plugin.Plo
	-rm -f ./$(DEPDIR)/kernel_netlink_shared.Plo
	-rm -f ./$(DEPDIR)/kernel_netlink_tests-kernel_netlink_shared.Po
	-rm -f ./$(DEPDIR)/kernel_netlink_tests-tests.Po
	-rm -f ./$(DEPDIR)/kernel_netlink_xfrmi.Plo
	-rm -f suites/$(DEPDIR)/kernel_netlink_tests-test_socket.Po
	-rm -f Makefile
distclean-am: clean-am distclean-compile distclean-generic \
	distclean-tags

dvi: dvi-am

dvi-am:

html: html-am

html-am:

info: info-am

info-am:

install-data-am: install-pluginLTLIBRARIES

install-dvi: install-dvi-am

install-dvi-am:

install-exec-am:

install-html: install-html-am

install-html-am:

install-info: install-info-am

install-info-am:

install-man:

install-pdf: install-pdf-am

install-pdf-am:

install-ps: install-ps-am

install-ps-am:

installcheck-am:

maintainer-clean: maintainer-clean-am
		-rm -f ./$(DEPDIR)/kernel_netlink_ipsec.Plo
	-rm -f ./$(DEPDIR)/kernel_netlink_net.Plo
	-rm -f ./$(DEPDIR)/kernel_netlink_plugin.Plo
	-rm -f ./$(DEPDIR)/kernel_netlink_shared.Plo
	-rm -f ./$(DEPDIR)/kernel_netlink_tests-kernel_netlink_shared.Po
	-rm -f ./$(DEPDIR)/kernel_netlink_tests-tests.Po
	-rm -f ./$(DEPDIR)/kernel_netlink_xfrmi.Plo
	-rm -f suites/$(DEPDIR)/kernel_netlink_tests-test_socket.Po
	-rm -f Makefile
maintainer-clean-am: distclean-am maintainer-clean-generic

mostlyclean: mostlyclean-am

mostlyclean-am: mostlyclean-compile mostlyclean-generic \
	mostlyclean-libtool

pdf: pdf-am

pdf-am:

ps: ps-am

ps-am:

uninstall-am: uninstall-pluginLTLIBRARIES

.MAKE: check-am install-am install-strip

.PHONY: CTAGS GTAGS TAGS all all-am am--depfiles check check-TESTS \
	check-am clean clean-checkPROGRAMS clean-generic clean-libtool \
	clean-noinstLTLIBRARIES clean-pluginLTLIBRARIES cscopelist-am \
	ctags ctags-am distclean distclean-compile distclean-generic \
	distclean-libtool distclean-tags distdir dvi dvi-am html \
	html-am info info-am install install-am install-data \
	install-data-am install-dvi install-dvi-am install-exec \
	install-exec-am install-html install-html-am install-info \
	install-info-am install-man install-pdf install-pdf-am \
	install-pluginLTLIBRARIES install-ps install-ps-am \
	install-strip installcheck installcheck-am installdirs \
	maintainer-clean maintainer-clean-generic mostlyclean \
	mostlyclean-compile mostlyclean-generic mostlyclean-libtool \
	pdf pdf-am ps ps-am tags tags-am uninstall uninstall-am \
	uninstall-pluginLTLIBRARIES

.PRECIOUS: Makefile


# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
