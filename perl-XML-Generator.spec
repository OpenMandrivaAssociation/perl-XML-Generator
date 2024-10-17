%define	upstream_name 	 XML-Generator
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A module to help in generating XML documents from perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} is a module to help in generating XML documents or in
producing DOM trees .

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc README Changes 
%{perl_vendorlib}/XML/*
%{_mandir}/man3/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.40.0-1mdv2011
+ Revision: 690333
- update to new version 1.04

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 408860
- update to 1.03

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 401860
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.01-3mdv2009.0
+ Revision: 242244
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2008.0
+ Revision: 52530
- update to new version 1.01

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2008.0
+ Revision: 46708
- update to new version 1.0

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.99-3mdv2008.0
+ Revision: 23515
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.99-2mdk
- Fix According to perl Policy
	- Source URL
	- URL
- use mkrel

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.99-1mdk
- 0.99
- drop redundant requires

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 0.93-5mdk
- Use %%makeinstall_std now that it works on klama

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 0.93-4mdk
- mv rm buildroot from %%prep to %%install
- macroification
- use %%makeinstall
- man path
- perllocal.pod

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.93-3mdk
- rebuild for new auto{prov,req}

