#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-lzf
Version  : 1.6.8
Release  : 13
URL      : https://pecl.php.net/get/LZF-1.6.8.tgz
Source0  : https://pecl.php.net/get/LZF-1.6.8.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause PHP-3.01
Requires: php-lzf-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
DESCRIPTION
LZF is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The module is self-contained and very small.

%package lib
Summary: lib components for the php-lzf package.
Group: Libraries

%description lib
lib components for the php-lzf package.


%prep
%setup -q -n LZF-1.6.8
cd %{_builddir}/LZF-1.6.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/lzf.so
