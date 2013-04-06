# kdelibs3 review: http://bugzilla.redhat.com/248899

%define _default_patch_fuzz 2

%define distname "Fedora"

%if 0%{?rhel}
%define distname "EL"
%endif

%define kde_settings 1 

%define arts_ev 8:1.5.10
%define qt3 qt3
%define qt3_version 3.3.8b
%define qt3_ev %{?qt3_epoch}%{qt3_version} 
%define qt3_docdir %{_docdir}/qt-devel-%{qt3_version}

%define kde_major_version 3

%define apidocs 1

# We always include this here now because kdeartwork 4 has moved on to
# icon-naming-spec names (partially, so the icon theme isn't usable with KDE 4
# yet either). Maybe the conditional should be dropped entirely? -- Kevin
%define include_crystalsvg 1

Summary: KDE 3 Libraries
Name:    kdelibs3
Version: 3.5.10
Release: 23%{?dist}.goose.2

License: LGPLv2
Url: http://www.kde.org/
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdelibs-%{version}.tar.bz2
Source1: kde.sh
Source2: kde.csh
Source3: devices.protocol

Patch1: kdelibs-3.5.1-xdg-menu.patch
Patch2: kdelibs-3.0.0-ndebug.patch
Patch4: kdelibs-3.0.4-ksyscoca.patch
Patch5: kdelibs-3.5.10-openssl.patch
Patch15: kdelibs-3.4.91-buildroot.patch
Patch32: kdelibs-3.2.3-cups.patch
Patch33: kdelibs-3.3.2-ppc.patch
Patch34: kdelibs-3.4.0-qtdoc.patch
Patch35: kdelibs-3.4.92-inttype.patch
Patch37: kdelibs-3.5.2-kdebug-kmail-quiet.patch
Patch38: kdelibs-3.5.2-cupsdconf2-group.patch
Patch39: kdelibs-3.5.4-kabc-make.patch
Patch40: kdelibs-3.5.4-kdeprint-utf8.patch
Patch41: kdelibs-3.5.6-utempter.patch
Patch43: kdelibs-3.5.6-lang.patch
Patch45: kdelibs-3.5.7-autostart.patch
Patch46: kdelibs-3.5.8-kate-vhdl.patch
Patch48: kdelibs-3.5.8-kspell-hunspell.patch
Patch49: kdelibs-3.5.8-kspell2-enchant.patch
Patch50: kdelibs-3.5.8-kspell2-no-ispell.patch
Patch51: kdelibs-3.5.9-cupsserverbin.patch
# initial support for (Only|Not)ShowIn=KDE3
Patch52: kdelibs-3.5.9-KDE3.patch
# use /usr/libexec/kde4/drkonqi in KCrash (#453243)
Patch53: kdelibs-3.5.9-drkonqi-kde4.patch
# fix build against Rawhide kernel headers (fix flock and flock64 redefinition)
Patch54: kdelibs-3.5.9-fix-flock-redefinition.patch
# update the KatePart latex.xml syntax definition to the version from Kile 2.0.3
Patch55: kdelibs-3.5.10-latex-syntax-kile-2.0.3.patch

# use /etc/kde in addition to /usr/share/config, borrowed from debian
Patch100: kdelibs-3.5.5-kstandarddirs.patch
# http://bugs.kde.org/93359, alternative to export libltdl_cv_shlibext=".so" hack.
Patch101: kde-3.5-libtool-shlibext.patch
# kget ignores simultaneous download limit (kde #101956)
Patch103: kdelibs-3.5.0-101956.patch
Patch104: kdelibs-3.5.10-gcc44.patch
Patch105: kdelibs-3.5.10-ossl-1.x.patch
Patch106: kdelibs-3.5.10-kio.patch
Patch107: kdelibs-3.5.10-assert.patch
Patch108: kdelibs-3.5.10-dtoa.patch
Patch109: kdelibs-3.5.10-kabc.patch
Patch110: arts-acinclude.patch
# kde4.4 backport
Patch111: kdelibs-3.5.10-kde-config_kde-version.patch

## security fixes
# fix CVE-2009-2537 - select length DoS
Patch200: kdelibs-3.5.10-cve-2009-2537-select-length.patch
# fix CVE-2009-1725 - crash, possible ACE in numeric character references
Patch201: kdelibs-3.5.10-cve-2009-1725.patch
# fix CVE-2009-1690 - crash, possible ACE in KHTML (<head> use-after-free)
Patch202: kdelibs-3.5.4-CVE-2009-1687.patch
# fix CVE-2009-1687 - possible ACE in KJS (FIXME: still crashes?)
Patch203: kdelibs-3.5.4-CVE-2009-1690.patch
# fix CVE-2009-1698 - crash, possible ACE in CSS style attribute handling
Patch204: kdelibs-3.5.10-cve-2009-1698.patch
# fix CVE-2009-2702 - ssl incorrect verification of SSL certificate with NUL in subjectAltName
Patch205: kdelibs-3.5.10-CVE-2009-2702.patch
# fix oCERT-2009-015 - unrestricted XMLHttpRequest access to local URLs
Patch206: kdelibs-3.5.10-oCERT-2009-015-xmlhttprequest.patch
# CVE-2009-3736, libltdl may load and execute code from a library in the current directory
Patch207: libltdl-CVE-2009-3736.patch

Requires: hicolor-icon-theme
%if %{kde_settings}
Requires: kde-settings >= 3.5
%endif
Requires: kde-filesystem
Requires: kdelibs-common
Requires: redhat-menus
Requires: shadow-utils
BuildRequires: sudo
Requires(hint): sudo

%if 0%{?fedora}
%define libkdnssd libkdnssd
%endif
%define BuildRequires: xorg-x11-proto-devel libX11-devel
%define _with_rgbfile --with-rgbfile=%{_datadir}/X11/rgb.txt
Requires: iceauth

Requires(pre): coreutils
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: hunspell

BuildRequires: gettext
BuildRequires: pcre-devel
BuildRequires: cups-devel cups
BuildRequires: %{qt3}-devel %{qt3}-devel-docs
BuildRequires: arts-devel >= %{arts_ev}
BuildRequires: flex >= 2.5.4a-13
BuildRequires: doxygen
BuildRequires: libxslt-devel
BuildRequires: sgml-common
BuildRequires: openjade
BuildRequires: jadetex
BuildRequires: docbook-dtd31-sgml
BuildRequires: docbook-style-dsssl
BuildRequires: perl-SGMLSpm
BuildRequires: docbook-utils
BuildRequires: zlib-devel
BuildRequires: libidn-devel
BuildRequires: audiofile-devel
BuildRequires: openssl-devel
BuildRequires: perl
BuildRequires: gawk
BuildRequires: byacc
BuildRequires: libart_lgpl-devel
BuildRequires: bzip2-devel
BuildRequires: libtiff-devel
BuildRequires: libacl-devel libattr-devel
BuildRequires: enchant-devel
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: db4-devel
BuildRequires: alsa-lib-devel
BuildRequires: pkgconfig
BuildRequires: glibc-kernheaders
BuildRequires: libutempter-devel
BuildRequires: findutils
BuildRequires: jasper-devel
BuildRequires: OpenEXR-devel
BuildRequires: automake

%if "%{name}" != "kdelibs" && "%{?apidocs}" != "1"
Obsoletes: kdelibs-apidocs < 6:%{version}-%{release}
%endif

%if 0%{?include_crystalsvg}
Provides: crystalsvg-icon-theme = 1:%{version}-%{release}
Obsoletes: crystalsvg-icon-theme < 1:%{version}-%{release}
%else
# for bootstrapping kde3, omit Requires: crystalsvg... -- Rex
Requires: crystalsvg-icon-theme
%endif


%description
Libraries for KDE 3:
KDE Libraries included: kdecore (KDE core library), kdeui (user interface),
kfm (file manager), khtmlw (HTML widget), kio (Input/Output, networking),
kspell (spelling checker), jscript (javascript), kab (addressbook),
kimgio (image manipulation).

%package devel
Group: Development/Libraries
Summary: Header files and documentation for compiling KDE 3 applications.
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{qt3}-devel
Requires: openssl-devel
Requires: arts-devel
%{?libkdnssd:Requires: libkdnssd-devel}
%description devel
This package includes the header files you will need to compile
applications for KDE 3.

%package apidocs
Group: Development/Documentation
Summary: KDE 3 API documentation.
Requires: %{name} = %{?epoch:%{epoch}:}%{version}
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the KDE 3 API documentation in HTML
format for easy browsing


%prep
%setup -q -n kdelibs-%{version}

%patch1 -p1 -b .xdg-menu
%patch2 -p1 -b .debug
%patch4 -p1 -b .ksyscoca
%patch5 -p1 -b .openssl
%patch15 -p1 -b .buildroot
%patch32 -p1 -b .cups
%patch33 -p1 -b .ppc
%patch34 -p1 -b .qtdoc
%patch35 -p1 -b .inttype
%patch37 -p1 -b .kdebug-kmail-quiet
%patch38 -p1 -b .cupsdconf2-group
%patch39 -p1 -b .kabc-make
%patch40 -p1 -b .kdeprint-utf8
%patch41 -p1 -b .utempter
%patch43 -p1 -b .lang
%patch45 -p1 -b .xdg-autostart
%patch46 -p1 -b .kate-vhdl
%patch48 -p1 -b .kspell
%patch49 -p1 -b .kspell2
%patch50 -p1 -b .no-ispell
%patch51 -p1 -b .cupsserverbin
%patch52 -p1 -b .KDE3
%patch53 -p1 -b .drkonqi-kde4
%patch54 -p1 -b .flock-redefinition
%patch55 -p1 -b .latex-syntax

%patch100 -p1 -b .kstandarddirs
%patch101 -p1 -b .libtool-shlibext
%patch104 -p1 -b .gcc44
%patch105 -p1 -b .ossl-1.x
%patch106 -p1 -b .kio
%patch107 -p1 -b .assert
%patch108 -p1 -b .alias
%patch109 -p1 -b .kabc
%patch110 -p1 -b .autoconf
%patch111 -p1 -b .kde-config_kde-version

# security fixes
%patch200 -p1 -b .cve-2009-2537
%patch201 -p0 -b .cve-2009-1725
%patch202 -p1 -b .cve-2009-1687
%patch203 -p1 -b .cve-2009-1690
%patch204 -p1 -b .cve-2009-1698
%patch205 -p1 -b .cve-2009-2702
%patch206 -p0 -b .oCERT-2009-015-xmlhttprequest
%patch207 -p1 -b .CVE-2009-3736

sed -i -e "s,^#define KDE_VERSION_STRING .*,#define KDE_VERSION_STRING \"%{version}-%{release} %{distname}\"," kdecore/kdeversion.h

# hack/fix for newer automake
sed -iautomake -e 's|automake\*1.10\*|automake\*1.1[0-5]\*|' admin/cvs.sh
make -f admin/Makefile.common cvs


%build
unset QTDIR && . /etc/profile.d/qt.sh

export QTDOC=%{qt3_docdir}

if [ -x /etc/profile.d/krb5.sh ]; then
  . /etc/profile.d/krb5.sh
elif ! echo ${PATH} | grep -q /usr/kerberos/bin ; then
  export PATH=/usr/kerberos/bin:${PATH}
fi

%if "%{name}" != "kdelibs"
export DO_NOT_COMPILE="libkscreensaver"
%endif

%configure \
   --includedir=%{_includedir}/kde \
   --disable-rpath \
   --enable-new-ldflags \
   --disable-dependency-tracking \
   %{!?debug: --disable-debug --disable-warnings --enable-final} \
   %{?debug:--enable-debug --enable-warnings --disable-final} \
   --disable-fast-malloc \
%if "%{_lib}" == "lib64"
  --enable-libsuffix="64" \
%endif
   --enable-cups \
   --enable-mitshm \
   --enable-pie \
   --enable-sendfile \
   --with-distribution="$(cat /etc/redhat-release 2>/dev/null)" \
   --with-alsa \
   --without-aspell \
   --without-hspell \
   --disable-libfam \
   --enable-dnotify \
   --enable-inotify \
   --with-utempter \
   %{?_with_rgbfile} \
   --with-jasper \
   --with-openexr \
   --with-xinerama

%if 0%{?apidocs}
  doxygen -s -u admin/Doxyfile.global
  make %{?_smp_mflags} apidox
%endif

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make DESTDIR=%{buildroot} install

# create/own, see http://bugzilla.redhat.com/483318
mkdir -p %{buildroot}%{_libdir}/kconf_update_bin

chmod a+x %{buildroot}%{_libdir}/*
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/services/devices.protocol

%if 0%{?apidocs}
pushd %{buildroot}%{_docdir}
ln -sf HTML/en/kdelibs-apidocs %{name}-devel-%{kde_major_version}
popd
%endif

# Make symlinks relative
pushd %{buildroot}%{_docdir}/HTML/en
for i in *; do
   if [ -d $i -a -L $i/common ]; then
      rm -f $i/common
      ln -sf ../common $i
   fi
done
popd

%if 0%{?fedora} < 12 && 0%{?rhel} < 6
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/kde.sh
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/kde.csh
%endif

# Use hicolor-icon-theme rpm/pkg instead (#178319)
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/

# ghost'd files
touch $RPM_BUILD_ROOT%{_datadir}/services/ksycoca

# remove references to extraneous/optional libraries in .la files (#170602)
# fam, libart_lgpl, pcre, libidn, libpng, libjpeg, libdns_sd, libacl/libattr, alsa-lib/asound
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" | xargs \
 sed -i \
 -e "s@-lfam@@g" \
 -e "s@%{_libdir}/libfam.la@@g" \
 -e "s@-lart_lgpl_2@@g" \
 -e "s@%{_libdir}/libpcreposix.la@@g" \
 -e "s@-lpcreposix@@g" \
 -e "s@-lpcre@@g" \
 -e "s@-lidn@@g" \
 -e "s@%{_libdir}/libidn.la@@g" \
 -e "s@-lpng@@g" \
 -e "s@-ljpeg@@g" \
 -e "s@%{_libdir}/libjpeg.la@@g" \
 -e "s@-ldns_sd@@g" \
 -e "s@-lacl@@g" \
 -e "s@%{_libdir}/libacl.la@@g" \
 -e "s@/%{_lib}/libacl.la@@g" \
 -e "s@-lattr@@g" \
 -e "s@%{_libdir}/libattr.la@@g" \
 -e "s@/%{_lib}/libattr.la@@g" \
 -e "s@-lasound@@g"  \
 -e "s@-lutempter@@g"

# libkdnssd bits
rm -f %{buildroot}%{_libdir}/libkdnssd.la
%{?libkdnssd:rm -rf %{buildroot}{%{_libdir}/libkdnssd.*,%{_includedir}/kde/dnssd}}

# remove conflicts with kdelibs-4
rm -f %{buildroot}%{_bindir}/checkXML
rm -f %{buildroot}%{_bindir}/ksvgtopng
rm -f %{buildroot}%{_bindir}/kunittestmodrunner
rm -f %{buildroot}%{_datadir}/config/kdebug.areas
rm -f %{buildroot}%{_datadir}/config/kdebugrc
rm -f %{buildroot}%{_datadir}/config/ui/ui_standards.rc
rm -f %{buildroot}%{_docdir}/HTML/en/common/1.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/10.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/2.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/3.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/4.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/5.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/6.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/7.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/8.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/9.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/artistic-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/bottom-left.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/bottom-middle.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/bottom-right.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/bsd-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/doxygen.css
rm -f %{buildroot}%{_docdir}/HTML/en/common/favicon.ico
rm -f %{buildroot}%{_docdir}/HTML/en/common/fdl-license
rm -f %{buildroot}%{_docdir}/HTML/en/common/fdl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/fdl-notice.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/footer.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/gpl-license
rm -f %{buildroot}%{_docdir}/HTML/en/common/gpl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/header.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/kde-default.css
rm -f %{buildroot}%{_docdir}/HTML/en/common/kde_logo_bg.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/lgpl-license
rm -f %{buildroot}%{_docdir}/HTML/en/common/lgpl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/mainfooter.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/mainheader.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/qpl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-left.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-middle.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-right-konqueror.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-right.jpg
rm -f %{buildroot}%{_docdir}/HTML/en/common/x11-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/xml.dcl
rm -rf %{buildroot}%{_datadir}/locale/all_languages
rm -rf %{buildroot}%{_sysconfdir}/xdg/menus/
rm -rf %{buildroot}%{_datadir}/autostart/
rm -f %{buildroot}%{_datadir}/config/colors/40.colors
rm -f %{buildroot}%{_datadir}/config/colors/Rainbow.colors
rm -f %{buildroot}%{_datadir}/config/colors/Royal.colors
rm -f %{buildroot}%{_datadir}/config/colors/Web.colors
rm -f %{buildroot}%{_datadir}/config/ksslcalist
rm -f %{buildroot}%{_bindir}/preparetips

# don't show kresources
sed -i -e "s,^OnlyShowIn=KDE;,OnlyShowIn=KDE3;," %{buildroot}%{_datadir}/applications/kde/kresources.desktop 

%if 0%{?include_crystalsvg} == 0
# remove all crystalsvg icons for now
rm -rf %{buildroot}%{_datadir}/icons/crystalsvg/
%endif


%check
ERROR=0
%if 0%{?apidocs}
if [ ! -f %{buildroot}%{_docdir}/HTML/en/kdelibs-apidocs/index.html ]; then
  echo "ERROR: %{_docdir}/HTML/en/kdelibs-apidocs/index.html not generated"
  ERROR=1
fi 
%endif
exit $ERROR


%clean
rm -rf %{buildroot}


%post
/sbin/ldconfig
%if 0%{?include_crystalsvg}
touch --no-create %{_datadir}/icons/crystalsvg 2> /dev/null || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg 2> /dev/null || :
%endif
%{_bindir}/update-desktop-database > /dev/null 2>&1 || :

%postun
/sbin/ldconfig
%if 0%{?include_crystalsvg}
touch --no-create %{_datadir}/icons/crystalsvg 2> /dev/null || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg 2> /dev/null || :
%endif
%{_bindir}/update-desktop-database > /dev/null 2>&1 || :


%files
%defattr(-,root,root,-)
%doc README
%doc COPYING.LIB
%if 0%{?fedora} < 12 && 0%{?rhel} < 6
%config(noreplace) %{_sysconfdir}/profile.d/*
%endif
%{_bindir}/artsmessage
%{_bindir}/cupsdconf
%{_bindir}/cupsdoprint
%{_bindir}/dcop
%{_bindir}/dcopclient
%{_bindir}/dcopfind
%{_bindir}/dcopobject
%{_bindir}/dcopquit
%{_bindir}/dcopref
%{_bindir}/dcopserver
%{_bindir}/dcopserver_shutdown
%{_bindir}/dcopstart
%{_bindir}/filesharelist
%{_bindir}/fileshareset
%{_bindir}/imagetops
%{_bindir}/kab2kabc
%{_bindir}/kaddprinterwizard
%{_bindir}/kbuildsycoca
%{_bindir}/kcmshell
%{_bindir}/kconf_update
%{_bindir}/kcookiejar
%{_bindir}/kde-config
%{_bindir}/kde-menu
%{_bindir}/kded
%{_bindir}/kdeinit
%{_bindir}/kdeinit_shutdown
%{_bindir}/kdeinit_wrapper
%{_bindir}/kdesu_stub
%{_bindir}/kdontchangethehostname
%{_bindir}/kdostartupconfig
%{_bindir}/kfile
%{_bindir}/kfmexec
%{_bindir}/khotnewstuff
%{_bindir}/kinstalltheme
%{_bindir}/kio_http_cache_cleaner
%{_bindir}/kio_uiserver
%{_bindir}/kioexec
%{_bindir}/kioslave
%{_bindir}/klauncher
%{_bindir}/kmailservice
%attr(4755,root,root) %{_bindir}/kpac_dhcp_helper
%{_bindir}/ksendbugmail
%{_bindir}/kshell
%{_bindir}/kstartupconfig
%{_bindir}/ktelnetservice
%{_bindir}/ktradertest
%{_bindir}/kwrapper
%{_bindir}/lnusertemp
%{_bindir}/make_driver_db_cups
%{_bindir}/make_driver_db_lpr
%{_bindir}/meinproc
%{_bindir}/start_kdeinit
%{_bindir}/start_kdeinit_wrapper
%attr(4755,root,root) %{_bindir}/kgrantpty
%{_libdir}/lib*.so.*
%{_libdir}/libkdeinit_*.so
%{_libdir}/lib*.la
%{_libdir}/kconf_update_bin/
%{_libdir}/kde3/
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/*
%exclude %{_datadir}/apps/ksgmltools2/
%config(noreplace) %{_datadir}/config/*
%{_datadir}/emoticons/*
%{_datadir}/icons/default.kde
%{_datadir}/mimelnk/magic
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%ghost %{_datadir}/services/ksycoca
%{_docdir}/HTML/en/kspell
%{_docdir}/HTML/en/common/*
%if 0%{?include_crystalsvg}
%{_datadir}/icons/crystalsvg/
%endif

%files devel
%defattr(-,root,root,-)
%{_bindir}/dcopidl*
%{_bindir}/kconfig_compiler
%{_bindir}/makekdewidgets
%{_datadir}/apps/ksgmltools2/
%{_includedir}/kde/
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%exclude %{_libdir}/libkdeinit_*.so

%if 0%{?apidocs}
%files apidocs
%defattr(-,root,root,-)
%{_docdir}/%{name}-devel-%{kde_major_version}
%{_docdir}/HTML/en/kdelibs*
%endif


%changelog
* Thu Jun 10 2010 Clint Savage <herlo@gooseproject.org> - 3.5.10-23.goose.2
- Apply updates from 3.5.10-24 committed by Rex Dieter (rhbz#681901)
- drop old Obsoletes/Provides: kdelibs(-devel/-apidocs)
- -apidocs: Requires: kde-filesystem

* Thu Jun 10 2010 Clint Savage <herlo@gooseproject.org> - 3.5.10-23.goose.1
- -apidocs: Requires: kde-filesystem

* Wed Jan 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-23
- patch for kde-config --kde-version option (kde#224540)

* Wed Dec 16 2009 Jaroslav Reznik <jreznik@redhat.com> - 3.5.10-22
- Repositioning the KDE Brand (#547361)

* Mon Dec 07 2009 Than Ngo <than@redhat.com> - 3.5.10-21
- fix security issues in libltdl bundle within kdelibs CVE-2009-3736
- backport upstream patches
- patch autoconfigury to build with autoconf >= 2.64 (Stepan Kasal)

* Mon Nov  2 2009 Lukáš Tinkl <ltinkl@redhat.com> - 3.5.10-20
- fix unrestricted XMLHttpRequest access to local URLs (oCERT-2009-015), #532428

* Mon Sep 28 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-19
- Conflicts with kde-settings (#526109)

* Mon Sep 28 2009 Than Ngo <than@redhat.com> - 3.5.10-18
- rhel cleanup

* Wed Sep 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-17 
- move /etc/profile.d/kde.(sh|csh) to kde-settings (F-12+)

* Fri Sep 04 2009 Than Ngo <than@redhat.com> - 3.5.10-16
- openssl-1.0 build fixes

* Fri Sep 04 2009 Than Ngo <than@redhat.com> - 3.5.10-15
- fix for CVE-2009-2702

* Thu Sep 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-14
- kde.(sh|csh): drop KDE_IS_PRELINKED (workaround bug #515539)

* Sun Jul 26 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-13
- fix CVE-2009-2537 - select length DoS
- fix CVE-2009-1725 - crash, possible ACE in numeric character references
- fix CVE-2009-1690 - crash, possible ACE in KHTML (<head> use-after-free)
- fix CVE-2009-1687 - possible ACE in KJS (FIXME: still crashes?)
- fix CVE-2009-1698 - crash, possible ACE in CSS style attribute handling

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-12 
- FTBFS kdelibs3-3.5.10-11.fc11 (#511571)
- -devel: Requires: %%{name}%%_isa ...

* Sun Apr 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-11
- update openssl patch (for 0.9.8k)

* Thu Apr 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-10
- move designer plugins to runtime (#487622)
- make -apidocs noarch

* Mon Mar 02 2009 Than Ngo <than@redhat.com> - 3.5.10-9
- enable -apidocs

* Fri Feb 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-8
- disable -apidocs (f11+, #487719)
- cleanup unused kdeui_symlink hack baggage

* Wed Feb 25 2009 Than Ngo <than@redhat.com> - 3.5.10-7
- fix files conflicts with 4.2.x
- fix build issue with gcc-4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 6:3.5.10-5
- unowned dirs (#483318)

* Sat Jan 10 2009 Ville Skyttä <ville.skytta at iki.fi> - 6:3.5.10-4
- Slight speedup to profile.d/kde.sh (#465370).

* Mon Dec 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.10-3
- update the KatePart latex.xml syntax definition to the version from Kile 2.0.3

* Thu Dec 04 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-2
- omit libkscreensaver (F9+)

* Tue Aug 26 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-1
- kde-3.5.10

* Fri Aug 22 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.9-18
- fix build against Rawhide kernel headers (fix flock and flock64 redefinition)

* Fri Aug 22 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.9-17
- fix logic error in OnlyShowIn=KDE3 patch

* Wed Jul 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.9-16
- f9+: use drkonqi from KDE 4 kdebase-runtime in KCrash (#453243)

* Wed Jun 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.9-15
- set include_crystalsvg to 1 everywhere
- use Epoch 1 for crystalsvg-icon-theme, add Obsoletes

* Tue Jun 03 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-14
- revert kdeui symlink hack (there be dragons) 
- unbreak -apidocs, add %%check so this never ever happens again

* Sat May 24 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-13
- f9+: include kdeui symlink here + scriptlets to help rpm handle it

* Fri May 23 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-12
- f9+: omit %%{_datadir}/apps/kdeui, use version from kdelibs-common (rh#447965, kde#157850)

* Thu May 15 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-11
- (Only|Not)ShowIn=KDE3 patch (helps #446466)

* Thu May 15 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-10
- fix kresources.desktop: NoDisplay=true

* Mon Apr 14 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-8
- omit Requires: kdndsd-avahi (#441222)

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-7
- more qt->qt3 fixes

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-6
- s/qt-devel/qt3-devel/

* Mon Mar 10 2008 Than Ngo <than@redhat.com> 3.5.9-5
- apply upstream patch to fix regression in kate (bz#436384)

* Tue Mar 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-4
- hardcode qt_ver again because 3.3.8b reports itself as 3.3.8 (fixes apidocs)

* Tue Feb 26 2008 Lukáš Tinkl <ltinkl@redhat.com> - 3.5.9-3
- #230979: Writes ServerBin into cupsd.conf
- #416101: unable to print after configuring printing in KDE

* Sat Feb 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-2
- F9+: include %%{_docdir}/HTML/en/common files which are not in kdelibs-common

* Thu Feb 14 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-1
- kde-3.5.9

* Mon Feb 11 2008 Than Ngo <than@redhat.com> 3.5.8-24
- make kresources hidden on f9+

* Sat Feb 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-23
- rebuild for GCC 4.3

* Sat Dec 22 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.8-22
- BR enchant-devel instead of aspell-devel on F9+ (FeatureDictionary)
- Requires: hunspell on F9+ (FeatureDictionary)
- patch KSpell for hunspell support on F9+ (FeatureDictionary)
- add and build enchant backend for KSpell2 (backported from Sonnet) on F9+
  (FeatureDictionary)
- don't build aspell and ispell backends for KSpell2 on F9+ (FeatureDictionary)

* Fri Dec 21 2007 Lukáš Tinkl <ltinkl@redhat.com> - 3.5.8-21
- updated Flash patch

* Mon Dec 17 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.8-20
- Requires: kdelibs-common (F9+) (#417251)

* Thu Dec 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-19
- flash fix (#410651, kde#132138, kde#146784)
- simplify crystalsvg-icon-theme handling

* Tue Dec 11 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-18
- set include_crystalsvg to 0 on F9+ (it comes from kdeartwork now)

* Tue Dec 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-17
- update openssl patch

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-16
- install profile scripts as 644 instead of 755 (Ville Skyttä, #407521)
- don't rename profile scripts to kde3.(c)sh (not worth the breakage)

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-15
- separate include_crystalsvg conditional, set to 1 until we have kdeartwork 4
- don't run icon %%post/%%postun snippets for crystalsvg if we don't ship it
- add "3" in all summaries and descriptions

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-14
- fix inverted logic for Requires: crystalsvg-icon-theme

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-13
- don't hardcode %%fedora

* Wed Nov 21 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.5.8-12
- renew the list of file conflicts and removals

* Tue Nov 20 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.5.8-11
- preserve makekdewidgets and kconf_compiler for fedora > 9
- add Requires: crystalsvg-icon-theme (for kdelibs3)

* Sun Nov 18 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.5.8-10
- only include and provide crystalsvg-icon-theme for fedora < 9

* Sun Nov 18 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.5.8-9
- add switch to force rpmbuild behavior for testing
- prepare %%files for non-conflicting kdelibs3

* Tue Oct 30 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-8
- Provides: crystalsvg-icon-theme

* Thu Oct 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-7
- fix application of custom zoom patch (rh#335461)

* Tue Oct 23 2007 Than Ngo <than@redhat.com> - 3.5.8-6
- Resolves: rh#335461, kpdf and kview lost custom zoom

* Thu Oct 18 2007 Than Ngo <than@redhat.com> - 3.5.8-5
- bz273681, add vhdl syntax for kate, thanks to Chitlesh GOORAH

* Wed Oct 17 2007 Than Ngo <than@redhat.com> 3.5.8-4
- apply upstream patch to fix http-regression

* Mon Oct 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.8-3
- respin (for openexr-1.6.0)

* Fri Oct 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.8-2
- kde-3.5.8

* Tue Sep 25 2007 Than Ngo <than@redhat.com> - 6:3.5.7-23
- fix rh#243611, autostart from XDG_CONFIG_DIRS

* Sat Sep 09 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 6:3.5.7-22
- Remove Conflicts: kdelibs4-devel, let kdelibs4 decide whether we conflict
  (allows using the old /opt/kde4 versions for now)

* Wed Aug 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.7-21
- vcard30 patch (kde#115219,rh#253496)
- -devel: restore awol Requires (< f8 only) (#253801)
- License: LGPLv2

* Wed Aug 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.7-20
- CVE-2007-3820, CVE-2007-4224, CVE-2007-4225
- clarify licensing

* Tue Aug 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.7-19
- ConsoleKit-related patch (#244065) 

* Sun Aug 12 2007 Florian La Roche <laroche@redhat.com> 6:3.5.7-18
- fix apidocs subpackage requires

* Mon Aug 06 2007 Than Ngo <than@redhat.com> - 6:3.5.7-17
- cleanup

* Fri Aug 03 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-16
- undo kdelibs3 rename (for now, anyway)
- move to -devel: checkXML, kconfig_compiler, (make)kdewidgets, ksgmltools2,
  ksvgtopng, kunittestmodrunner
- set KDE_IS_PRELINKED unconditionally (#244065)
- License: LGPLv2+

* Fri Jul 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-15
- Obsoletes/Provides: kdelibs-apidocs (kdelibs3)

* Fri Jul 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-14
- toggle kdelibs3 (f8+)

* Wed Jul 18 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-13
- build fails against cups-1.3 (#248717)
- incorporate kdelibs3 bits (not enabled... yet) 

* Wed Jul 18 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-10
- +Requires: kde-filesystem

* Mon Jul 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-9
- omit ICEauthority patch (kde#147454, rh#243560, rh#247455)

* Wed Jun 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-8
- rework previously botched openssl patch

* Wed Jun 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-7
- -devel: Provides: kdelibs3-devel = ...
- openssl patch update (portability)
- drop deprecated ssl-krb5 patch

* Sat Jun 16 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-6
- Provides: kdelibs3 = %%version-%%release

* Sat Jun 16 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-5
- -devel: +Requires: libutempter-devel

* Fri Jun 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-4
- omit lib_loader patch (doesn't apply cleanly)

* Fri Jun 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-3
- include experimental libtool patches

* Mon Jun 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-2
- kdesu: sudo support (kde bug #20914), Requires(hint): sudo

* Wed Jun 06 2007 Than Ngo <than@redhat.com> -  6:3.5.7-0.1.fc7
- 3.5.7

* Thu May 24 2007 Than Ngo <than@redhat.com> 6:3.5.6-10.fc7
- don't change permission .ICEauthority by sudo KDE programs
- apply patch to fix locale issue
- apply upstream patch to fix kde#146105

* Thu May 16 2007 Rex Dieter <rdieter[AT]fedorproject.org> - 6:3.5.6-9
- make qtdocdir handling robust
- kde_settings=1
- Req: -desktop-backgrounds-basic

* Wed May 16 2007 Than Ngo <than@redhat.com> - 3.5.6-8.fc7
- add correct qt-version to build kde apidocs ,bz#239947
- disable kde_settings

* Thu May 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-7
- BR: +keyutils-libs-devel (until krb5 is fixed, bug #240220)

* Thu May 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-6
- kde.sh: fix typo/thinko

* Thu May 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-5
- %%changelog: prune pre-kde3 entries
- %%ghost %%{_datadir}/services/ksycoca
- omit extraneous .la file references (#178733)
- BR: jasper-devel OpenEXR-devel
- xdg-menu compat symlinks (to help transition to using XDG_MENU_PREFIX)
- fix kde#126812.patch to be non-empty
- cleanup kde.(sh|csh)
- Requires: +kde-settings -redhat-artwork 
- make apidocs build optional (default on)
- use FHS-friendly /etc/kde (#238136)

* Mon Mar 26 2007 Than Ngo <than@redhat.com> - 6:3.5.6-3.fc7
- apply upstream patch to fix build issue with qt-3.3.8
- apply upstream patch to to fix crash on particular 404 url
  in embedded HTML viewer

* Tue Feb 27 2007 Than Ngo <than@redhat.com> - 6:3.5.6-2.fc7
- cleanup specfile

* Mon Feb 05 2007 Than Ngo <than@redhat.com> - 6:3.5.6-1.fc7
- 3.5.6
- apply patch to fix #225420, CVE-2007-0537 Konqueror improper
  HTML comment rendering, thanks to Dirk Müller, KDE security team

* Tue Nov 14 2006 Than Ngo <than@redhat.com> - 6:3.5.5-1.fc7
- rebuild

* Fri Oct 27 2006 Than Ngo <than@redhat.com> 6:3.5.5-0.2
- add missing api docs

* Wed Oct 25 2006 Than Ngo <than@redhat.com> 6:3.5.5-0.1
- update to 3.5.5

* Sun Oct 01 2006 Than Ngo <than@redhat.com> 6:3.5.4-10
- fix utf8 issue in kdeprint
- fix #178320,#198828, follow menu-spec
- upstream patches,
   fix #106748, Evaluate scripts in <iframe src=javascript:..> in the right context
   fix #133071, Crash when characterSet was accessed on newly-created document

* Sat Sep 30 2006 Than Ngo <than@redhat.com> 6:3.5.4-9
- fix #178320,#198828, follow menu-spec
- fix #119167, page rendered incorrectly at larger font sizes

* Tue Sep 26 2006 <than@redhat.com> 6:3.5.4-8
- fix #115891/bz#208270, CUPS 1.2.x unix socket support
- apply upstream patches
   fix #123915, Page format display is 'overlaid'
   fix #100188, Fix incorrect 'endl' usage

* Thu Sep 14 2006 Than Ngo <than@redhat.com> 6:3.5.4-7
- apply upstream patches
   fix #132678, Google search encoding fix
   khtml rendering issue
   fix #134118, silent startup notification never going away
   fix #133401, crash when attempting to remove a standard shortcut that isn't actually in 
   the KStdAccel::ShortcutList
   fix #131979, unbreak "latest" and "most downloads" views

* Tue Sep 12 2006 Than Ngo <than@redhat.com> 6:3.5.4-6
- fix #205767, konsole no longer register itself to utmp
- fix #123941, qt xim plugin sometimes leads to crash

* Tue Sep 05 2006 Than Ngo <than@redhat.com> 6:3.5.4-5
- apply upstream patches
   fix #123413, kded crash when KDED modules make DCOP calls in their destructors
   fix #133529, konqueror's performance issue
   fix kdebug crash
   more icon contexts (Tango icontheme)
   fix #133677, file sharing doesn't work with 2-character long home directories

* Mon Sep 04 2006 Than Ngo <than@redhat.com> 6:3.5.4-4
- apply upstream patches
   fix kde#121528, konqueror crash

* Wed Aug 23 2006 Than Ngo <than@redhat.com> 6:3.5.4-3
- apply upstream patches
   fix kde#131366, Padding-bottom and padding-top not applied to inline elements
   fix kde#131933, crash when pressing enter inside a doxygen comment block
   fix kde#106812, text-align of tables should only be reset in quirk mode
   fix kde#90462, konqueror crash while rendering in khtml

* Tue Aug 08 2006 Than Ngo <than@redhat.com> 6:3.5.4-2
- add BR on gettext, cups

* Tue Aug 08 2006 Than Ngo <than@redhat.com> 6:3.5.4-1
- rebuilt

* Wed Jul 26 2006 Petr Rockai <prockai@redhat.com> - 6:3.5.4-0.pre2
- drop the gcc workaround, problem fixed in gcc/g++

* Mon Jul 24 2006 Petr Rockai <prockai@redhat.com> - 6:3.5.4-0.pre1
- prerelease of 3.5.4 (from the first-cut tag)
- disable --enable-final on s390x, seems to cause problems

* Thu Jul 20 2006 Than Ngo <than@redhat.com> 6:3.5.3-11
- apply upstream patches,
   fix kde#130831, remember when the last replacement string was the empty string

* Tue Jul 18 2006 Petr Rockai <prockai@redhat.com> - 6:3.5.3-10
- do not ship the dummy kdnssd implementation, depend on external one
  (there is one provided by kdnssd-avahi now)
- change the use of anonymous namespace in kedittoolbar.h, so that
  the KEditToolbar classes are exported again

* Mon Jul 17 2006 Petr Rockai <prockai@redhat.com>
- should have been 6:3.5.3-9 but accidentally built as 6:3.5.3-8.fc6
- --disable-libfam and --enable-inotify to get inotify support
  and to disable gamin/fam usage
- add %{?dist} to Release:

* Tue Jul 11 2006 Than Ngo <than@redhat.com> 6:3.5.3-8
- upstream patches,
    kde#130605 - konqueror crash
    kde#129187 - konqueror crash when modifying address bar address

* Mon Jul 10 2006 Than Ngo <than@redhat.com> 6:3.5.3-7
- apply upstream patches,
    kde#123307 - Find previous does nothing sometimes
    kde#106795 - konqueror crash

* Tue Jul 04 2006 Than Ngo <than@redhat.com> 6:3.5.3-6
- apply upstream patches, fix #128940/#81806/#128760

* Sat Jun 24 2006 Than Ngo <than@redhat.com> 6:3.5.3-5
- fix #196013, mark kde.sh/kde.csh as config file
- fix #178323 #196225, typo in kde.sh
- apply upstream patches

* Thu Jun 08 2006 Than Ngo <than@redhat.com> 6:3.5.3-4
- enable --enable-new-ldflags again since ld bug fixed
- move only *.so symlinks to -devel subpackage

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 6:3.5.3-3
- move .so symlinks to -devel subpackage

* Thu Jun 01 2006 Than Ngo <than@redhat.com> 7:3.5.3-2
- drop --enable-new-ldflags, workaround for ld bug

* Wed May 31 2006 Than Ngo <than@redhat.com> 7:3.5.3-1
- update to 3.5.3

* Tue May 23 2006 Than Ngo <than@redhat.com> 7:3.5.2-7
- fix #189677, No longer possible to "copy & rename" file in same directory

* Mon May 22 2006 Than Ngo <than@redhat.com> 6:3.5.2-6
- fix #192585, kdeprint writes incorrect cupsd.conf

* Thu May 18 2006 Than Ngo <than@redhat.com> 6:3.5.2-5
- use a versioned Obsoletes for kdelibs-docs

* Tue May 16 2006 Than Ngo <than@redhat.com> 6:3.5.2-4 
- rebuild against new qt to fix multilib issue
- fix #178323, add KDE_IS_PRELINKED/KDE_NO_IPV60
 
* Wed May 03 2006 Than Ngo <than@redhat.com> 6:3.5.2-3
- fix #173235, disable kmail debug info #173235
- use XDG_CONFIG_DIRS for kde menu #178320
- don't use private API with newer CUPS >=1.2

* Fri Apr 21 2006 Than Ngo <than@redhat.com> 6:3.5.2-2
- apply patch to fix crash kdeprint

* Tue Mar 21 2006 Than Ngo <than@redhat.com> 6:3.5.2-1
- update to 3.5.2

* Tue Feb 21 2006 Than Ngo <than@redhat.com> 6:3.5.1-2.3
- apply patch to fix missing icons in KDE main menu
- requires redhat-artwork >= 0.239-2
- don't own /usr/share/icons/hicolor #178319
- remove broken links #154093 

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.1-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.1-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Feb 02 2006 Than Ngo <than@redhat.com> 6:3.5.1-2 
- add Obsolete: kdelibs-docs

* Wed Feb 01 2006 Than Ngo <than@redhat.com> 6:3.5.1-1
- 3.5.1

* Thu Jan 19 2006 Than Ngo <than@redhat.com> 6:3.5.0-6
- rename subpackage to -apidocs

* Wed Jan 18 2006 Than Ngo <than@redhat.com> 6:3.5.0-5
- apply patch to fix a printing problem
- add subpackage kdelibs-docs
- enable --enable-new-ldflags #161074 

* Wed Dec 21 2005 Than Ngo <than@redhat.com> 6:3.5.0-4
- apply patch to fix crash in kicker on KDE logout

* Fri Dec 16 2005 Than Ngo <than@redhat.com> 6:3.5.0-3
- add requires on several devel subpackages

* Tue Dec 13 2005 Than Ngo <than@redhat.com> 6:3.5.0-2 
- apply patch to fix konqueror for working with new openssl #174541 

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
* - rebuilt

* Thu Dec 01 2005 Than Ngo <than@redhat.com> 6:3.5.0-1
- add fix for modular X, thanks to Ville Skyttä #174131
- probably fix #174541

* Mon Nov 28 2005 Than Ngo <than@redhat.com> 6:3.5.0-0.1.rc2
- 3.5 rc2

* Mon Nov 14 2005 Than Ngo <than@redhat.com> 6:3.5.0-0.1.rc1
- update 3.5.0 rc1
- remove unneeded lnusertemp workaround
- remove references to optional libraries in .la files #170602 

* Thu Nov 10 2005 Than Ngo <than@redhat.com> 6:3.4.92-4
- apply patch to fix gcc4 compilation

* Wed Nov 09 2005 Than Ngo <than@redhat.com> 6:3.4.92-3 
- rebuilt against new libcrypto, libssl
- requires iceauth
 
* Fri Nov 04 2005 Than Ngo <than@redhat.com> 6:3.4.92-2
- move lnusertemp in arts, workaround for #169631

* Mon Oct 24 2005 Than Ngo <than@redhat.com> 6:3.4.92-1
- update to 3.5 beta 2

* Wed Oct 12 2005 Than Ngo <than@redhat.com> 6:3.4.91-2
- add libacl-devel buildrequirement
- add openoffice mimelnk files #121769

* Tue Sep 27 2005 Than Ngo <than@redhat.com> 6:3.4.91-1
- update to KDE 3.5 Beta1

* Mon Aug 08 2005 Than Ngo <than@redhat.com> 6:3.4.2-2
- add requires xorg-x11 #165287

* Mon Aug 01 2005 Than Ngo <than@redhat.com> 6:3.4.2-1
- update to 3.4.2

* Tue Jun 21 2005 Than Ngo <than@redhat.com> 6:3.4.1-2
- add devices protocol #160927

* Wed May 25 2005 Than Ngo <than@redhat.com> 6:3.4.1-1
- 3.4.1

* Wed May 04 2005 Than Ngo <than@redhat.com> 6:3.4.0-6
- kimgio input validation vulnerabilities, CAN-2005-1046

* Wed Apr 13 2005 Than Ngo <than@redhat.com> 6:3.4.0-5
- more fixes from CVS stable branch
- fix kbuildsycoca crashes with signal 11 on kde startup #154246

* Tue Apr 12 2005 Than Ngo <than@redhat.com> 6:3.4.0-4
- add workaround for #154294

* Thu Apr 07 2005 Than Ngo <than@redhat.com> 3.4.0-3
- add missing kcontrol/khelp/home/find in main menu #151655 
- fix bad symlinks #154093

* Fri Apr 01 2005 Than Ngo <than@redhat.com> 6:3.4.0-2
- more patches from CVS stable branch
- add missing kde documents, workaround for rpm bug

* Thu Mar 17 2005 Than Ngo <than@redhat.com> 6:3.4.0-1
- 3.4.0 release

* Wed Mar 16 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.6
- new snapshot from KDE_3_4_BRANCH

* Mon Mar 14 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.5
- default font setting Sans/Monospace

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.4
- rebuilt against gcc-4.0.0-0.31

* Tue Mar 01 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.3
- fix dependency problem with openssl-0.9.7e

* Tue Mar 01 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.2
- rebuilt against gcc-4

* Sat Feb 26 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.1
- bump release

* Fri Feb 25 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.0
- KDE 3.4.0 rc1

* Tue Feb 22 2005 Than Ngo <than@redhat.com> 6:3.3.92-0.3
- respin KDE 3.4 beta2

* Thu Feb 17 2005 Than Ngo <than@redhat.com> 6:3.3.92-0.2
- Add symlinks to crystal icons, thanks Peter Rockai, #121929
- fix export

* Mon Feb 14 2005 Than Ngo <than@redhat.com> 6:3.3.92-0.1
- KDE 3.4 Beta2

* Sat Feb 12 2005 Than Ngo <than@redhat.com> 6:3.3.2-0.7
- backport CVS patch, cleanup InputMethod

* Fri Feb 11 2005 Than Ngo <than@redhat.com> 6:3.3.2-0.6
- drop mktemp patch

* Thu Feb 10 2005 Than Ngo <than@redhat.com> 6:3.3.2-0.5
- use mkstemp instead of mktemp
- fix knotify crash after applying sound system change
- add steve cleanup patch

* Wed Dec 15 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.4
- get rid of broken AltiVec instructions on ppc

* Tue Dec 14 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.3
- apply the patch to fix Konqueror Window Injection Vulnerability #142510
  CAN-2004-1158,  Thanks to KDE security team
- Security Advisory: plain text password exposure, #142487
  thanks to KDE security team

* Wed Dec 08 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.2
- workaround for compiler bug on ia64 (-O0)

* Fri Dec 03 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.1
- update to 3.3.2
- remove unneeded kdelibs-3.3.1-cvs.patch, kdelibs-3.3.1-xml.patch

* Tue Nov 02 2004 Than Ngo <than@redhat.com> 6:3.3.1-4
- backport CVS patches, fix konqueror crash #134758

* Fri Oct 29 2004 Than Ngo <than@redhat.com> 6:3.3.1-3
- add some fixes from CVS

* Sat Oct 16 2004 Than Ngo <than@redhat.com> 6:3.3.1-2
- rebuilt for rhel

* Wed Oct 13 2004 Than Ngo <than@redhat.com> 6:3.3.1-1
- update to KDE 3.3.1

* Wed Sep 29 2004 Than Ngo <than@redhat.com> 6:3.3.0-5
- add missing requires on libidn-devel

* Sun Sep 26 2004 Than Ngo <than@redhat.com> 6:3.3.0-4
- cleanup menu

* Mon Sep 20 2004 Than Ngo <than@redhat.com> 3.3.0-3
- fix a bug in ksslopen #114835

* Tue Sep 07 2004 Than Ngo <than@redhat.com> 6:3.3.0-2
- add patch to fix KDE trash always full #122988

* Thu Aug 19 2004 Than Ngo <than@redhat.com> 6:3.3.0-1
- update to 3.3.0 release

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 6:3.3.0-0.1.rc2
- update to 3.3.0 rc1

* Sun Aug 08 2004 Than Ngo <than@redhat.com> 6:3.3.0-0.1.rc1
- update to 3.3 rc1

* Fri Jul 23 2004 Than Ngo <than@redhat.com> 3.2.92-2
- update to KDE 3.3 Beta 2
- remove some unneeded patch files
- enable libsuffix

* Mon Jul 19 2004 Than Ngo <than@redhat.com> 6:3.2.3-6
- add IM patch
- set kprinter default to cups

* Mon Jul 12 2004 Than Ngo <than@redhat.com> 6:3.2.3-5
- rebuild

* Mon Jul 05 2004 Than Ngo <than@redhat.com> 6:3.2.3-4
- built with libpcre support, it's needed for using regular expressions in Javascript code bug #125264

* Thu Jul 01 2004 Than Ngo <than@redhat.com> 6:3.2.3-3
- fix double entry in filelist
- add some devel packages in requires

* Thu Jun 17 2004 Than Ngo <than@redhat.com> 3.2.3-2
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 31 2004 Than Ngo <than@redhat.com> 3.2.3-1
- update to KDE 3.2.3
- remove some patch files, which are now included in 3.2.3

* Mon May 17 2004 Than Ngo <than@redhat.com> 6:3.2.2-7
- add patch to enable PIE

* Sun May 16 2004 Than Ngo <than@redhat.com> 6:3.2.2-6
- vulnerability in the mailto handler, CAN-2004-0411

* Fri May 14 2004 Than Ngo <than@redhat.com> 3.2.2-5
- KDE Telnet URI Handler File Vulnerability , CAN-2004-0411

* Wed Apr 21 2004 Than Ngo <than@redhat.com> 3.2.2-4
- Implements the FreeDesktop System Tray Protocol, thanks to Harald Hoyer

* Mon Apr 19 2004 Than Ngo <than@redhat.com> 3.2.2-3
- fix #120265 #119642

* Sun Apr 18 2004 Warren Togami <wtogami@redhat.com> 3.2.2-2
- #120265 #119642 -devel req alsa-lib-devel esound-devel fam-devel
                             glib2-devel libart_lgpl-devel
- #88853 BR autoconf automake libpng-devel libvorbis-devel
            glib2-devel libtiff-devel
- cups-libs explicit epoch, some cleanups

* Tue Apr 13 2004 Than Ngo <than@redhat.com> 3.2.2-1
- 3.2.2 release

* Fri Mar 12 2004 Than Ngo <than@redhat.com> 6:3.2.1-1.4
- rebuild

* Thu Mar 11 2004 Than Ngo <than@redhat.com> 6:3.2.1-1.3
- get rid of application.menu, it's added in redhat-menus

* Fri Mar 05 2004 Than Ngo <than@redhat.com> 6:3.2.1-1.2
- respin

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Than Ngo <than@redhat.com> 3.2.1-1
- update to 3.2.1 release

* Tue Feb 17 2004 Than Ngo <than@redhat.com> 6:3.2.0-1.5
- fix typo bug, _smp_mflags instead smp_mflags

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 09 2004 Than Ngo <than@redhat.com> 6:3.2.0-0.4
- add new icon patch file 

* Thu Feb 05 2004 Than Ngo <than@redhat.com> 6:3.2.0-0.3 
- build against qt 3.3.0
- fix a bug in ksslopen on x86_64, bug #114835

* Tue Feb 03 2004 Than Ngo <than@redhat.com> 6:3.2.0-0.2
- 3.2.0 release

* Fri Jan 23 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.4
- fixed #114114

* Wed Jan 21 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.3
- fixed file conflict with hicolor-icon-theme
- added requires: hicolor-icon-theme

* Tue Jan 20 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.2
- added kde.sh, kde.csh
- fixed build problem
- fixed rpm file list

* Mon Jan 19 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.1
- KDE 3.2 RC1

* Tue Dec 02 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.2
- KDE 3.2 Beta2 respin

* Mon Dec 01 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.1
- KDE 3.2 Beta2

* Wed Nov 26 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.4
- add missing cupsdconf, cupsdoprint and dcopquit

* Tue Nov 25 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.3
- enable alsa support

* Sat Nov 08 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.2
- cleanup several patch files

* Mon Nov 03 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.1
- 3.2 Beta 1
- remove many patches, which are now in upstream
- adjust many redhat specific patch files
- cleanup rpm file list

* Fri Oct 17 2003 Than Ngo <than@redhat.com> 6:3.1.4-4
- fixed icon scale patch, thanks to Thomas Wörner

* Fri Oct 10 2003 Than Ngo <than@redhat.com> 6:3.1.4-3
- better icon scale patch

* Thu Oct 02 2003 Than Ngo <than@redhat.com> 6:3.1.4-2
- rebuild against new gcc-3.3.1-6, fixed miscompiled code on IA-32 

* Mon Sep 29 2003 Than Ngo <than@redhat.com> 6:3.1.4-1
- 3.1.4

* Thu Sep 04 2003 Than Ngo <than@redhat.com> 6:3.1.3a-1
- 3.1.3a

* Thu Aug 28 2003 Than Ngo <than@redhat.com> 6:3.1.3-8
- adopted a patch file from Mandrake, it fixes full screen problem

* Wed Aug 27 2003 Than Ngo <than@redhat.com> 6:3.1.3-7
- rebuilt

* Wed Aug 27 2003 Than Ngo <than@redhat.com> 6:3.1.3-6
- rebuilt

* Fri Aug 22 2003 Than Ngo <than@redhat.com> 6:3.1.3-5
- fix build problem with gcc 3.x

* Wed Aug 06 2003 Than Ngo <than@redhat.com> 6:3.1.3-4
- rebuilt

* Wed Aug 06 2003 Than Ngo <than@redhat.com> 6:3.1.3-3
- add patch file to fix horizontal scrollbar issue

* Thu Jul 31 2003 Than Ngo <than@redhat.com> 6:3.1.3-2
- rebuilt

* Tue Jul 29 2003 Than Ngo <than@redhat.com> 6:3.1.3-1
- 3.1.3
- add Prereq: dev

* Tue Jun 17 2003 Than Ngo <than@redhat.com> 6:3.1.2-7
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun May 18 2003 Than Ngo <than@redhat.com> 6:3.1.2-5
- remove workaround for glibc bug

* Wed May 14 2003 Than Ngo <than@redhat.com> 6:3.1.2-3
- fix dependence bug

* Tue May 13 2003 Than Ngo <than@redhat.com> 6:3.1.2-2
- fix a bug in loading openssl library

* Mon May 12 2003 Than Ngo <than@redhat.com> 6:3.1.2-1
- 3.1.2

* Wed Apr 30 2003 Than Ngo <than@redhat.com> 6:3.1.1-7
- build with -fpic on ppc (ld bugs)

* Mon Apr 28 2003 Than Ngo <than@redhat.com> 6:3.1.1-6
- libjpeg-devel and bzip2-devel in buildrequires (#89635)

* Thu Apr 24 2003 Than Ngo <than@redhat.com> 6:3.1.1-5
- use pcre native API

* Mon Apr 14 2003 Than Ngo <than@redhat.com> 6:3.1.1-4
- add xrandr support

* Sun Apr 13 2003 Than Ngo <than@redhat.com> 6:3.1.1-3
- PS/PDF file handling vulnerability

* Thu Mar 20 2003 Than Ngo <than@redhat.com> 6:3.1.1-2
- add patch file from CVS to fix: https authentication through proxy fails
- add patch file from CVS to fix: KZip fails for some .zip archives

* Sun Mar 16 2003 Than Ngo <than@redhat.com> 6:3.1.1-1
- 3.1.1 stable release
- move desktop-create-kmenu to kdelibs

* Mon Mar  3 2003 Than Ngo <than@redhat.com> 6:3.1-12
- lan redirect

* Mon Feb 24 2003 Than Ngo <than@redhat.com> 6:3.1-11
- add Buildprereq libart_lgpl-devel

* Mon Feb 24 2003 Than Ngo <than@redhat.com> 6:3.1-10
- move API documentation into kdelibs-devel (#84976)

* Fri Feb 21 2003 Than Ngo <than@redhat.com> 6:3.1-9
- add fix from Thomas Wörner to watch /usr/share/applications
  for changes, (bug #71613)

* Thu Feb 20 2003 Than Ngo <than@redhat.com> 6:3.1-8
- rebuid against gcc 3.2.2 to fix dependency in la file

* Thu Feb 13 2003 Thomas Woerner <twoerner@redhat.com> 6:3.1-7
- fixed arts bug #82750, requires rebuild of kdelibs

* Tue Feb 11 2003 Than Ngo <than@redhat.com> 6:3.1-6
- fix Norway i18n issue, bug #73446

* Mon Feb 10 2003 Than Ngo <than@redhat.com> 6:3.1-5
- konqueror crashes on a double click, bug #81503

* Sun Feb  9 2003 Than Ngo <than@redhat.com> 6:3.1-4
- add patch to support the macromedia, bug #83808

* Thu Feb  6 2003 Than Ngo <than@redhat.com> 6:3.1-3
- add patch to set correct default encoding, bug #82539
- don't overwrite defaultstyle, bug #74795, #80103

* Fri Jan 31 2003 Than Ngo <than@redhat.com> 6:3.1-2
- Add better resize icon patch from Thomas Woerner

* Tue Jan 28 2003 Than Ngo <than@redhat.com> 6:3.1-1
- 3.1 final

* Sun Jan 26 2003 Than Ngo <than@redhat.com> 6:3.1-0.16
- use make apidox to create KDE api instead doxygen

* Thu Jan 24 2003 Than Ngo <than@redhat.com> 6:3.1-0.15
- use doxygen to create api docs
- clean up specfile

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 6:3.1-0.14
- rebuild

* Wed Jan 22 2003 Than Ngo <than@redhat.com> 3.1-0.13
- rc7

* Thu Jan 16 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.12
- added icon scale patch
- added ia64 again

* Mon Jan 13 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.11
- excluded ia64

* Sun Jan 12 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.10
- rebuild

* Fri Jan 10 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.9
- removed silly size_t check

* Fri Jan 10 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.8
- rc6

* Fri Jan 10 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.7
- ssl uses krb5

* Sat Dec 28 2002 Than Ngo <than@redhat.com> 3.1-0.6
- rebuild

* Mon Dec 16 2002 Than Ngo <than@redhat.com> 3.1-0.5
- rebuild

* Thu Dec 12 2002 Than Ngo <than@redhat.com> 3.1-0.4
- fix dependency bug
- use kdoc to create api docs

* Sat Nov 30 2002 Than Ngo <than@redhat.com> 3.1-0.3
- fix bug #78646
- set kde_major_version

* Fri Nov 22 2002 Than Ngo <than@redhat.com> 3.1-0.2
- use doxygen to create api docs

* Tue Nov 19 2002 Than Ngo <than@redhat.com> 3.1-0.1
- update rc4
- adjust many patch files for 3.1
- remove some patch files, which are now in 3.1

* Sun Nov 10 2002 Than Ngo <than@redhat.com> 3.0.5-1.1
- conform strict ANSI (bug #77603)

* Sat Nov  9 2002 Than Ngo <than@redhat.com> 3.0.5-1
- update to 3.0.5

* Wed Oct 16 2002 Than Ngo <than@redhat.com> 3.0.4-3
- rebuild to get rid of libstdc++.la on x86_64
- cleanup sepcfile
- dependency issue

* Sat Oct 12 2002 Than Ngo <than@redhat.com> 3.0.4-2
- better handling of desktop file renames (bug #74071)
- initLanguage issue

* Thu Oct 10 2002 Than Ngo <than@redhat.com> 3.0.4-1

- 3.0.4
- Added 2 patch files for built-in tests from AndreyPozdeev@rambler.ru (bug #75003)
- Added KDE Url (bug #54592)

* Tue Oct  8 2002 Than Ngo <than@redhat.com> 3.0.3-10
- Added fix to get correct Lib directory name on 64bit machine
- New fix to handle desktop file renames (bug #74071)

* Fri Sep 20 2002 Than Ngo <than@redhat.com> 3.0.3-8.1
- Konqueror Cross Site Scripting Vulnerability

* Sun Sep  1 2002 Than Ngo <than@redhat.com> 3.0.3-8
- remove merging share/applnk

* Sat Aug 31 2002 Than Ngo <than@redhat.com> 3.0.3-7
- put Red Hat in the version number
- desktop file issue

* Tue Aug 27 2002 Phil Knirsch <pknirsch@redhat.com> 3.0.3-6
- Removed gcc31 patch as it breaks the Netscape plugin in gcc32.

* Mon Aug 26 2002 Phil Knirsch <pknirsch@redhat.com> 3.0.3-5
- Use LANG env as default if available
- Fixed general language handling problems

* Sun Aug 25 2002 Than Ngo <than@redhat.com> 3.0.3-4
- revert about KDE, use preference

* Thu Aug 22 2002 Than Ngo <than@redhat.com> 3.0.3-3
- Added katetextbuffermultibyte patch from Leon Ho (bug #61464)
- build against new qt

* Tue Aug 13 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.3-2
- Update to 3.0.3 respin to fix SSL security bug

* Sun Aug 11 2002 Than Ngo <than@redhat.com> 3.0.3-1
- 3.0.3
- Added ksyscoca patch from Harald Hoyer

* Thu  Aug  8 2002 Than Ngo <than@redhat.com> 3.0.2-6
- Added better system tray dock patch from Harald Hoyer

* Fri Aug  2 2002 Than Ngo <than@redhat.com> 3.0.2-5
- Fixed a bug in ktip (bug #69627,70329)

* Fri Aug  2 2002 Than Ngo <than@redhat.com> 3.0.2-4
- Added system tray dock patch from Harald Hoyer
- Added Buildrequires audiofile-devel (bug #69983)
- Added Buildrequires openssl-devel (bug #64858)
- Rebuild against qt 3.0.5 (bug #70379)
- Added patch to remove "about KDE" menu item from help menu (bug #67287)
- Fixed dependencies bug by update (bug #69798)
- Added some bugfixes from 3.0.2 stable branches

* Fri Aug  2 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-3
- Add some bugfixes from CVS (mostly HTML rendering fixes)

* Mon Jul 22 2002 Tim Powers <timp@redhat.com> 3.0.2-2
- rebuild using gcc-3.2-0.1

* Tue Jul  2 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-1
- 3.0.2

* Tue Jun 25 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-0.cvs20020625.1
- Make KLocale respect the LANG setting when kpersonalizer wasn't run

* Mon Jun 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-0.cvs20020624.1
- Update, should be VERY close to 3.0.2 final now.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-0.cvs20020620.1
- Update
- Remove the malloc hack, it's no longer needed with glibc 2.2.90

* Tue May 28 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.1-3
- Add support for xdg-list icon theme spec

* Fri May  9 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.1-1
- 3.0.1

* Wed May  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-12
- Update to KDE_3_0_BRANCH
- Do away with the GCC296 define, it's handled automatically

* Thu May  2 2002 Than Ngo <than@redhat.com> 3.0.0-11
- add some fixes from KDE CVS
- build against gcc-3.1-0.26/qt-3.0.3-12

* Mon Apr 15 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-10
- Change sonames to something indicating the compiler version if a compiler
  < gcc 3.1 is used
- Add compat symlinks for binary compatibility with other distributions

* Thu Apr 11 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-9
- Fix Qt designer crash when loading KDE plugins

* Tue Apr  9 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-8
- Add build requirement on samba >= 2.2.3a-5 to make sure the correct
  smb ioslave can be built

* Mon Apr  8 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-7
- Merge the following fixes from KDE_3_0_BRANCH:
  - RFC 2818 compliance for KSSL
  - Detect premature loss of connection in http ioslave (this may have
    been the cause of the bugzilla CGI.pl:1444 issue)
  - Don't send SIGHUP to kdesu child applications
  - Fix KHTML form rendering problems

* Wed Apr  3 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-6
- Fix up timeout problems with form submissions (#62196)

* Wed Apr  3 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-5
- Merge kjs crash-on-invalid-input fix from KDE_3_0_BRANCH

* Thu Mar 28 2002 Than Ngo <than@redhat.com> 3.0.0-4
- fix kde version

* Thu Mar 28 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-3
- Add another khtml rendering fix

* Wed Mar 27 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-2
- Add a khtml fix from KDE_3_0_BRANCH, prevents form content from
  being submitted twice, which probably caused the CGI.pl:1444 bug
  some people have noted with Bugzilla.

* Wed Mar 27 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-1
- Update to final
- Add fixes from KDE_3_0_BRANCH
