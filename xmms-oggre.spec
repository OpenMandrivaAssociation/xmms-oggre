%define oname oggre
%define name xmms-%oname
%define version 0.3
%define release %mkrel 5

Summary: Ogg output plugin for xmms
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/my-xmms-plugs/%{oname}-%{version}.tar.bz2
License: GPL
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libvorbis-devel 
BuildRequires: libxmms-devel
BuildRequires: automake1.4
Requires: xmms
Provides: oggre
Obsoletes: oggre
URL: http://sourceforge.net/projects/my-xmms-plugs/

%description
This xmms plugin writes Ogg Vorbis audio files to the hard disk.

%prep
%setup -q -n %oname-%version
chmod 644 AUTHORS ChangeLog
aclocal-1.4 -I macros
autoconf

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/xmms/Output/liboggre.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%_libdir/xmms/Output/liboggre.so


