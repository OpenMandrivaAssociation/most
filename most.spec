%define name    most
%define version 4.10.2
%define release %mkrel 3

Summary:	More, less, most
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		ftp://space.mit.edu/pub/davis/%{name}
Group:		File tools
Source:		%{URL}/%{name}-%{version}.tar.bz2
BuildRequires:	libslang-devel chrpath
Requires:	slang

%description

most is a paging program that displays, one windowful  at  a  time,  the
contents of a file on a terminal. It pauses  after  each  windowful  and
prints on the window status line the screen the file name, current  line
number, and the percentage of the file so far displayed.


%prep
%setup -q


%build
%configure
%make
chrpath -d src/objs/most

%install
rm -rf $RPM_BUILD_ROOT
install -D -m0755 src/objs/most $RPM_BUILD_ROOT%{_bindir}/most
install -D -m0644 most.1        $RPM_BUILD_ROOT%{_mandir}/man1/most.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr (-,root,root)
%doc COPYRIGHT README  changes.txt most.doc most-fun.txt lesskeys.rc most.rc
%{_bindir}/most
%{_mandir}/man1/most.1*
