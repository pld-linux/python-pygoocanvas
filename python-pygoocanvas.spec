Summary:	Python bindings for GooCanvas
Summary(pl.UTF-8):	Wiązania języka Python do biblioteki GooCanvas
Name:		python-pygoocanvas
Version:	0.9.0
Release:	1
License:	LGPL v2
Group:		Libraries/Python
Source0:	http://download.berlios.de/pygoocanvas/pygoocanvas-%{version}.tar.gz
# Source0-md5:	1988b7572d553d954ffd159e7e61cb17
Patch0:		%{name}-pyc.patch
URL:		http://developer.berlios.de/projects/pygoocanvas/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.7
BuildRequires:	goocanvas-devel >= 0.9
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-pycairo-devel >= 1.2.0
BuildRequires:	python-pygobject-apidocs
BuildRequires:	python-pygobject-devel >= 2.11.3
BuildRequires:	python-pygtk-devel >= 2:2.10.0
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for GooCanvas.

%description -l pl.UTF-8
Wiązania języka Python do biblioteki GooCanvas.

%package apidocs
Summary:	pygoocanvas API documentation
Summary(pl.UTF-8):	Dokumentacja API pygoocanvas
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
pygoocanvas API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API pygoocanvas.

%prep
%setup -q -n pygoocanvas-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTMLdir=%{_gtkdocdir}/pygoocanvas

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{py_sitedir}/goocanvasmodule.so

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pygoocanvas
