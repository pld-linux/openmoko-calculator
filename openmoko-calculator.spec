#
Summary:	OpenMoko calculator applet
Name:		openmoko-calculator
Version:	0.0.0.2360
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	749e2d782cb5fd2368e7fa7e8ee9e2c6
URL:		http://openmoko.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libmatchbox-devel >= 1.8
BuildRequires:	openmoko-libs-devel
Requires:	openmoko-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define openmokoname %(echo %{name} | sed -e 's/openmoko-//')

%description
OpenMoko calculator applet

%prep
%setup -q

%build
cp /usr/share/automake/mkinstalldirs .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang Calculator

%clean
rm -rf $RPM_BUILD_ROOT

%files -f Calculator.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/openmoko-calculator
%{_desktopdir}/openmoko-calculator.desktop
%{_pixmapsdir}/openmoko-calculator.png
