%define oname	FileRunner

Summary:	A simple file manager with built-in FTP support
Name:		filerunner
Version:	10.12.28.23
Release:	%mkrel 1
License:	GPLv3+
Group:		File tools
URL:		http://sourceforge.net/projects/filerunner/
Source0:	http://downloads.sourceforge.net/project/%{name}/fr-10.12.28.23.tar.gz
BuildArch:	noarch
BuildRequires:	imagemagick
BuildRequires:	tcl-devel
Requires:	tcl
Requires:	tk
Provides:	%{oname} = %{version}-%{release}
Obsoletes:	%{oname} <= 2.5.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
FileRunner is a file manager for Unix. It is simple and efficient and has
a built-in FTP client. New and improved from a FileRunner of long ago.

%prep
%setup -q -c %{name}-%{version}

# http://qa.mandriva.com/show_bug.cgi?id=22193
find -type f | xargs perl -pi -e "s|\\\$glob\(doclib_fr\)|%{_docdir}/%{name}|g"

%build
#nothing

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{tcl_sitelib}/%{oname}/bitmaps
mkdir -p %{buildroot}%{_bindir}

cp -a bitmaps/* %{buildroot}%{tcl_sitelib}/%{oname}/bitmaps
cp -a *.tcl %{buildroot}%{tcl_sitelib}/%{oname}
cp -a icon.xpm %{buildroot}%{tcl_sitelib}/%{oname}
cp -a tclIndex %{buildroot}%{tcl_sitelib}/%{oname}

install -m755 fr %{buildroot}%{tcl_sitelib}/%{oname}/fr
install -m755 frftp %{buildroot}%{tcl_sitelib}/%{oname}/frftp

ln -s %{tcl_sitelib}/%{oname}/fr %{buildroot}%{_bindir}/fr
ln -s %{_docdir}/%{name}/HISTORY %{buildroot}%{tcl_sitelib}/%{oname}/HISTORY

# Icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps

convert icon.xpm -resize 16x16  %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert icon.xpm -resize 32x32  %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert icon.xpm -resize 48x48  %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=fr
Icon=%{name}
Terminal=false
Type=Application
Categories=Network;FileTransfer;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING FAQ HISTORY README *.txt
%{tcl_sitelib}/%{oname}
%{_bindir}/fr
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

