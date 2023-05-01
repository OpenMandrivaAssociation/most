Summary:	A powerful paging program
Name:		  most
Version:	5.2.0
Release:	1
License:	GPLv2
Group:		File tools
URL:		  https://www.jedsoft.org/releases/most/
Source0:		https://www.jedsoft.org/releases/most/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(slang)
BuildRequires:	chrpath
Requires:	slang

%description
most is a paging program that displays the contents of a file on a
terminal one windowful at a time. A status line indicating the file name,
current line number, and percentage of the file already displayed is also
shown.

%prep
%setup -q

# do not strip binaries
sed -i 's|\$(INSTALL) -s|\$(INSTALL)|' src/Makefile.in

%build
%configure \
	--with-slanglib=%{_libdir} \
	--with-slanginc=%{_includedir}/slang
%__make

chrpath -d src/objs/most

%install
%make_install

%files
%license COPYRIGHT COPYING
%{_docdir}/%{name}/
%{_bindir}/most
%{_mandir}/man1/most.1*


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 5.0.0a-5mdv2011.0
+ Revision: 612937
- the mass rebuild of 2010.1 packages

* Tue Feb 02 2010 Sandro Cazzaniga <kharec@mandriva.org> 5.0.0a-4mdv2010.1
+ Revision: 499788
- Fix summary
- Fix rpmlint warning

* Sat Dec 12 2009 Jérôme Brenier <incubusss@mandriva.org> 5.0.0a-3mdv2010.1
+ Revision: 477847
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Sep 05 2008 Lev Givon <lev@mandriva.org> 5.0.0a-1mdv2009.0
+ Revision: 281309
- Update to 5.0.0a.

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 4.10.2-5mdv2009.0
+ Revision: 252780
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 4.10.2-3mdv2008.1
+ Revision: 166023
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jun 06 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 4.10.2-3mdv2008.0
+ Revision: 36103
- Rebuild with libslang2.
- Import most




* Thu Oct 20 2005 Lenny Cartier <lenny@mandriva.com> 4.10.2-2mdk
- 4.10.2

* Mon May 10 2004 Michael Scherer <misc@mandrake.org> 4.9.4-1mdk
- New release 4.9.4
- remove rpath

* Fri Jan  2 2004 Han Boetes <han@linux-mandrake.com> 4.9.2-3mdk
- rebuild

* Fri Dec 27 2002 Han Boetes <han@linux-mandrake.com> 4.9.2-2mdk
- rebuild because of new rpm macros and new glibc

* Wed Aug 21 2002 Han Boetes <han@linux-mandrake.com> 4.9.2-1mdk
- First spec for mandrake.
