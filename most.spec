%define name	most
%define version	5.0.0a
%define release	%mkrel 5

Summary:	A powerful paging program
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
URL:		ftp://space.mit.edu/pub/davis/%{name}
Group:		File tools
Source:		%{URL}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libslang-devel chrpath
Requires:	slang

%description
most is a paging program that displays the contents of a file on a
terminal one windowful at a time. A status line indicating the file name,
current line number, and percentage of the file already displayed is also
shown.

%prep
%setup -q

%build
%configure
%make
chrpath -d src/objs/most

%install
%__rm -rf %{buildroot}
%__install -D -m0755 src/objs/most %{buildroot}%{_bindir}/most
%__install -D -m0644 most.1	%{buildroot}%{_mandir}/man1/most.1

%clean
%__rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc COPYRIGHT COPYING README changes.txt most.doc most-fun.txt lesskeys.rc most.rc
%{_bindir}/most
%{_mandir}/man1/most.1*
