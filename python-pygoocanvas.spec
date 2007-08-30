#
Summary:	Python bindings for GooCanvas
Name:		python-pygoocanvas
Version:	0.9.0
Release:	1
License:	GPLv2
Group:		Development/Libraries
Source0:	http://download.berlios.de/pygoocanvas/pygoocanvas-%{version}.tar.gz
# Source0-md5:	1988b7572d553d954ffd159e7e61cb17
Patch0:		%{name}-pyc.patch
URL:		http://developer.berlios.de/projects/pygoocanvas/
BuildRequires:	goocanvas-devel
BuildRequires:	python-devel
BuildRequires:	python-pygobject-apidocs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for GooCanvas

%package apidocs
Summary:	pygoocanvas API documentation
Summary(pl):	Dokumentacja API pygoocanvas
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
pygoocanvas API documentation.

%description apidocs -l pl
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTMLDIR='%{_gtkdocdir}/%{name}'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/goocanvasmodule.so

%files apidocs
%defattr(644,root,root,755)
%dir %{_datadir}/gtk-doc/html/pygoocanvas
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-ellipse-model.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-ellipse.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-group-model.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-group.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-image-model.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-image.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-item-model-simple.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-item-model.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-item-simple.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-item.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-misc.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-path-model.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-path.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-polyline-model.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-polyline.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-rect-model.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-rect.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-style.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-table-model.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-table.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-text-model.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-text.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas-widget.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-canvas.html
%{_datadir}/gtk-doc/html/pygoocanvas/class-hierarchy.html
%{_datadir}/gtk-doc/html/pygoocanvas/index.html
%{_datadir}/gtk-doc/html/pygoocanvas/index.sgml
%{_datadir}/gtk-doc/html/pygoocanvas/pygoocanvas-core-classes.html
%{_datadir}/gtk-doc/html/pygoocanvas/pygoocanvas-misc-items.html
%{_datadir}/gtk-doc/html/pygoocanvas/pygoocanvas-model-items.html
%{_datadir}/gtk-doc/html/pygoocanvas/pygoocanvas-std-items.html
%{_datadir}/gtk-doc/html/pygoocanvas/pygoocanvas.devhelp
%{_datadir}/gtk-doc/html/pygoocanvas/style.css
