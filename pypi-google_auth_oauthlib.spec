#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-google_auth_oauthlib
Version  : 0.7.1
Release  : 32
URL      : https://files.pythonhosted.org/packages/fb/d1/afcdd1611dc768ed3757a021a6e9410275ae27c6b26b84623bc0f9f706dc/google-auth-oauthlib-0.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/fb/d1/afcdd1611dc768ed3757a021a6e9410275ae27c6b26b84623bc0f9f706dc/google-auth-oauthlib-0.7.1.tar.gz
Summary  : Google Authentication Library
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-google_auth_oauthlib-bin = %{version}-%{release}
Requires: pypi-google_auth_oauthlib-license = %{version}-%{release}
Requires: pypi-google_auth_oauthlib-python = %{version}-%{release}
Requires: pypi-google_auth_oauthlib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(google_auth)
BuildRequires : pypi(requests_oauthlib)

%description
oauthlib integration for Google Auth
====================================
|pypi|

%package bin
Summary: bin components for the pypi-google_auth_oauthlib package.
Group: Binaries
Requires: pypi-google_auth_oauthlib-license = %{version}-%{release}

%description bin
bin components for the pypi-google_auth_oauthlib package.


%package license
Summary: license components for the pypi-google_auth_oauthlib package.
Group: Default

%description license
license components for the pypi-google_auth_oauthlib package.


%package python
Summary: python components for the pypi-google_auth_oauthlib package.
Group: Default
Requires: pypi-google_auth_oauthlib-python3 = %{version}-%{release}

%description python
python components for the pypi-google_auth_oauthlib package.


%package python3
Summary: python3 components for the pypi-google_auth_oauthlib package.
Group: Default
Requires: python3-core
Provides: pypi(google_auth_oauthlib)
Requires: pypi(google_auth)
Requires: pypi(requests_oauthlib)

%description python3
python3 components for the pypi-google_auth_oauthlib package.


%prep
%setup -q -n google-auth-oauthlib-0.7.1
cd %{_builddir}/google-auth-oauthlib-0.7.1
pushd ..
cp -a google-auth-oauthlib-0.7.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667576385
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-google_auth_oauthlib
cp %{_builddir}/google-auth-oauthlib-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-google_auth_oauthlib/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/google-oauthlib-tool

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-google_auth_oauthlib/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
