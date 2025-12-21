Summary:	VoIP framework
Name:		tapioca-xmpp
Version:	0.3.0
Release:	%mkrel 9
License:	LGPL
Group:		Video
URL:		https://sourceforge.net/projects/tapioca-voip
Source0:	http://dl.sf.net/tapioca-voip/%{name}-%{version}.tar.bz2
Patch0:		tapioca-xmpp-0.3.0-new_libjingle_libnames.diff
Requires:	tapioca
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	glib2-devel 
BuildRequires:  pkgconfig
BuildRequires:  libdbus-devel >= 0.36
BuildRequires:  libdbus-glib >= 0.36
BuildRequires:	tapioca-devel
BuildRequires:	libjingle-devel
BuildRequires:	autoconf2.5
BuildRequires:	automake
BuildRequires:	libtool
Buildroot:	%{_tmppath}/%{name}-buildroot 

%description
Tapioca is a framework for Voice over IP (VoIP) and Instant Messaging (IM). 
Its main goal is to provide an easy way for developing and using VoIP and IM 
services in any kind of application. It was designed to be cross-platform, 
lightweight, thread-safe, having mobile devices and applications in mind.

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/xmpp_connection_manager-0.3
%{_datadir}/dbus-1/services/org.tapioca.Xmpp.service
%{_datadir}/tapioca-0.3/xmpp.ini

#--------------------------------------------------------------------

%prep

%setup -q
%patch0 -p0

# lib64 fix
perl -pi -e "s|/lib\b|/%{_lib}|g" configure*

%build
rm -rf autom4te.cache
rm -f configure
libtoolize --copy --force; aclocal -I m4; automake --add-missing --copy --foreign; autoconf

%configure2_5x

%make

%install
rm -rf %buildroot

%makeinstall_std
# we do not want .la files
rm -f %buildroot/%{_libdir}/*.la

%clean
rm -rf %buildroot

