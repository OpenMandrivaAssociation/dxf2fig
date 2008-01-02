%define name dxf2fig
%define version 2.13
%define release %mkrel 3

Summary: Convert dxf files to xfig format
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Graphics
Url: http://ta.twi.tudelft.nl/ftp/dv/lemmens/
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
dxf2fig parses Autocad DXF input, then calls external
routines to do either plotting or a fig conversion for xfig.
The conversion is fairly complete. Layers (depths in xfig),
blocks (compounds in xfig), colors, and linetypes are roughly
preserved in the output file. 

%prep
%setup -q

%build
%make  CFLAGS="$RPM_OPT_FLAGS -DVERSION=\\\"\$(VERSION)\\\" -DMODDATE=\\\"\$(MODDATE)\\\""

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_bindir
cp dxf2fig %buildroot%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO Changelog
%_bindir/dxf2fig

