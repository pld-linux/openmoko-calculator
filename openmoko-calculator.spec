Summary:	OpenMoko calculator applet
Summary(pl.UTF-8):	Aplet kalkulatora dla OpenMoko
Name:		openmoko-calculator
Version:	0.0.0.2360
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	749e2d782cb5fd2368e7fa7e8ee9e2c6
URL:		http://openmoko.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	openmoko-libs-devel >= 0.0.1
BuildRequires:	pkgconfig
Requires:	openmoko-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenMoko calculator applet.

%description -l pl.UTF-8
Aplet kalkulatora dla OpenMoko.

%prep
%setup -q

%build
%{__glib_gettextize}
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
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/openmoko-calculator
%{_desktopdir}/openmoko-calculator.desktop
%{_pixmapsdir}/openmoko-calculator.png
