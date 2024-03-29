#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : libXScrnSaver
Version  : 1.2.4
Release  : 10
URL      : https://www.x.org/releases/individual/lib/libXScrnSaver-1.2.4.tar.gz
Source0  : https://www.x.org/releases/individual/lib/libXScrnSaver-1.2.4.tar.gz
Source1  : https://www.x.org/releases/individual/lib/libXScrnSaver-1.2.4.tar.gz.sig
Summary  : The XScrnSaver Library
Group    : Development/Tools
License  : MIT-Opengroup
Requires: libXScrnSaver-lib = %{version}-%{release}
Requires: libXScrnSaver-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32scrnsaverproto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(scrnsaverproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)

%description
XScreenSaver - X11 Screen Saver extension client library
--------------------------------------------------------

%package dev
Summary: dev components for the libXScrnSaver package.
Group: Development
Requires: libXScrnSaver-lib = %{version}-%{release}
Provides: libXScrnSaver-devel = %{version}-%{release}
Requires: libXScrnSaver = %{version}-%{release}

%description dev
dev components for the libXScrnSaver package.


%package dev32
Summary: dev32 components for the libXScrnSaver package.
Group: Default
Requires: libXScrnSaver-lib32 = %{version}-%{release}
Requires: libXScrnSaver-dev = %{version}-%{release}

%description dev32
dev32 components for the libXScrnSaver package.


%package lib
Summary: lib components for the libXScrnSaver package.
Group: Libraries
Requires: libXScrnSaver-license = %{version}-%{release}

%description lib
lib components for the libXScrnSaver package.


%package lib32
Summary: lib32 components for the libXScrnSaver package.
Group: Default
Requires: libXScrnSaver-license = %{version}-%{release}

%description lib32
lib32 components for the libXScrnSaver package.


%package license
Summary: license components for the libXScrnSaver package.
Group: Default

%description license
license components for the libXScrnSaver package.


%prep
%setup -q -n libXScrnSaver-1.2.4
cd %{_builddir}/libXScrnSaver-1.2.4
pushd ..
cp -a libXScrnSaver-1.2.4 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670224783
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1670224783
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libXScrnSaver
cp %{_builddir}/libXScrnSaver-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libXScrnSaver/dcc7cc194ef7fcd3e5f8e9bc20ddad371ee1d36c
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/scrnsaver.h
/usr/lib64/libXss.so
/usr/lib64/pkgconfig/xscrnsaver.pc
/usr/share/man/man3/XScreenSaverAllocInfo.3
/usr/share/man/man3/XScreenSaverGetRegistered.3
/usr/share/man/man3/XScreenSaverQueryExtension.3
/usr/share/man/man3/XScreenSaverQueryInfo.3
/usr/share/man/man3/XScreenSaverQueryVersion.3
/usr/share/man/man3/XScreenSaverRegister.3
/usr/share/man/man3/XScreenSaverSelectInput.3
/usr/share/man/man3/XScreenSaverSetAttributes.3
/usr/share/man/man3/XScreenSaverSuspend.3
/usr/share/man/man3/XScreenSaverUnregister.3
/usr/share/man/man3/XScreenSaverUnsetAttributes.3
/usr/share/man/man3/Xss.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXss.so
/usr/lib32/pkgconfig/32xscrnsaver.pc
/usr/lib32/pkgconfig/xscrnsaver.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXss.so.1
/usr/lib64/libXss.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXss.so.1
/usr/lib32/libXss.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libXScrnSaver/dcc7cc194ef7fcd3e5f8e9bc20ddad371ee1d36c
