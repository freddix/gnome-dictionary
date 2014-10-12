Summary:	Online dictionary
Name:		gnome-dictionary
Version:	3.14.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-dictionary/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	8c381246e832701c3b5168a6e5b79406
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows to look up an online dictionary for definitions and correct
spellings of words.

%package libs
Summary:	libgdict library
License:	LGPL v2
Group:		X11/Libraries

%description libs
libgdict library.

%package devel
Summary:	Header files for libgdict library
License:	LGPL v2
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
This is the package containing the header files for libgdict library.

%package apidocs
Summary:	libgdict API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgdict API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgdict-1.0.la

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%post 	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-dictionary
%{_desktopdir}/gnome-dictionary.desktop
%{_datadir}/gnome-dictionary
%{_datadir}/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%{_mandir}/man1/gnome-dictionary.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgdict-1.0.so.6
%attr(755,root,root) %{_libdir}/libgdict-1.0.so.*.*.*
%{_datadir}/gdict-1.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdict-1.0.so
%{_includedir}/gdict-1.0
%{_pkgconfigdir}/gdict-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdict
