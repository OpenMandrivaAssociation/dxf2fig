Summary:	Convert dxf files to xfig format
Name:		dxf2fig
Version:	2.13
Release:	7
License:	GPL
Group:		Graphics
Url:		http://ta.twi.tudelft.nl/ftp/dv/lemmens/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		dxf2fig-format-string.patch

%description
dxf2fig parses Autocad DXF input, then calls external
routines to do either plotting or a fig conversion for xfig.
The conversion is fairly complete. Layers (depths in xfig),
blocks (compounds in xfig), colors, and linetypes are roughly
preserved in the output file. 

%prep
%setup -q
%patch0 -p0 -b .fmt

%build
%make CFLAGS="%{optflags} -DVERSION=\\\"\$(VERSION)\\\" -DMODDATE=\\\"\$(MODDATE)\\\""

%install
mkdir -p %{buildroot}%{_bindir}
cp dxf2fig %{buildroot}%{_bindir}

%files
%doc README TODO Changelog
%{_bindir}/dxf2fig


