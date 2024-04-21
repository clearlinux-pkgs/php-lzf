#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-lzf
Version  : 1.7.0
Release  : 63
URL      : https://pecl.php.net/get/LZF-1.7.0.tgz
Source0  : https://pecl.php.net/get/LZF-1.7.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause PHP-3.01
Requires: php-lzf-lib = %{version}-%{release}
Requires: php-lzf-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
DESCRIPTION
LZF is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The module is self-contained and very small.

%package lib
Summary: lib components for the php-lzf package.
Group: Libraries
Requires: php-lzf-license = %{version}-%{release}

%description lib
lib components for the php-lzf package.


%package license
Summary: license components for the php-lzf package.
Group: Default

%description license
license components for the php-lzf package.


%prep
%setup -q -n LZF-1.7.0
cd %{_builddir}/LZF-1.7.0
pushd ..
cp -a LZF-1.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-lzf
cp %{_builddir}/LZF-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-lzf/23cb6fa873d559515b754db54720962118c95899 || :
cp %{_builddir}/LZF-%{version}/lib/LICENSE %{buildroot}/usr/share/package-licenses/php-lzf/9a0e277bb547589f33bbd1fc939e6057703a95ae || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/lzf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-lzf/23cb6fa873d559515b754db54720962118c95899
/usr/share/package-licenses/php-lzf/9a0e277bb547589f33bbd1fc939e6057703a95ae
