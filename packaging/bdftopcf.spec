Name:           bdftopcf
Version:        1.0.3
Release:        0
License:        MIT
Summary:        Font compiler for the X server and font server
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xfont)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
bdftopcf is a font compiler for the X server and font server. Fonts
in Portable Compiled Format can be read by any architecture, although
the file is structured to allow one particular architecture to read
them directly without reformatting. This allows fast reading on the
appropriate machine, but the files are still portable (but read more
slowly) on other machines.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1%{?ext_man}

%changelog
