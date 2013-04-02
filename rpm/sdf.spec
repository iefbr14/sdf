%define ver 2.001
%define rel 4

%{!?mkrel:%define mkrel(c:) %{-c:0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*)(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

Name:		sdf
Version:	%{ver}
Release:	%mkrel %rel
License:	BSD like
Group:		Publishing
Summary:	Simple Document Format document development system
Source:		%{name}-%{version}.tar.bz2
URL:		http://search.cpan.org/~ianc/%{name}-%{version}/
BuildRequires:	perl
BuildRequires:	perl-devel
BuildArch:	noarch

%description
SDF (Simple Document Format) is a freely available document development
system which generates high quality outputs in a variety of formats
from a single source. The output formats supported include
PostScript(tm), PDF, HTML, plain text, POD, man pages, LaTeX,
MIF, SGML, Windows(tm) help, RTF, MIMS F6 help and MIMS HTX help.
If the idea of specifying documents in a logical manner via a
simple markup language sounds appealing, SDF may be useful to you.

SDF documents are simple to create and maintain, minimising the time
spent on documentation. In particular, SDF directly supports the
creation and maintenance of large, on-line documentation systems
(including intranets) via centralised hypertext management and
rule-based hypertext generation. As well as normal documents,
SDF is useful for:

* user manuals (paper-based and online)
* online document catalogs
* Perl module documentation
* Delphi(tm) component documentation
* source code listings (pretty printing most languages).

SDF is also good for literate programming, i.e. documentation can
be embedded in the comments of most programming languages and can be
selectively extracted. The embedded documentation can be in any
markup language you like, although there are advantages to using
SDF's markup language.

SDF is freely available for commercial and non-commercial use.
See the LICENSE file for details.

%prep
%setup -q -n %{name}-%{version}

%build
perl Makefile.PL
%make

%install
%makeinstall_std INSTALLDIRS=vendor

%files
%{_bindir}/*
%{perl_vendorlib}/%{name}
%{perl_vendorlib}/Pod/*.pm
%{_mandir}/man?/*
%doc LICENSE README PODNOTES



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 2.001-4mdv2010.0
+ Revision: 433640
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.001-3mdv2008.1
+ Revision: 140782
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 03 2007 Buchan Milne <bgmilne@mandriva.org> 2.001-3mdv2008.0
+ Revision: 78636
- Force all installation dirs to vendor
- Rebuild


* Wed Dec 15 2004 Buchan Milne <bgmilne@linux-mandrake.com> 2.001-2mdk
- rebuild for cooker
- add distro-specific release tag

* Sun Jun 13 2004 Buchan Milne <bgmilne@linux-mandrake.com> 2.001-1mdk
- first Mandrake package

