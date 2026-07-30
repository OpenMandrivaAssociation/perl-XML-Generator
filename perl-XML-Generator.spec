%define	upstream_name 	 XML-Generator
%define upstream_version 1.13
Name:		perl-%{upstream_name}
Version:	1.13
Release:	2

Summary:	A module to help in generating XML documents from perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/timlegge/perl-XML-Generator
Source0:	https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/XML-Generator-1.13.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} is a module to help in generating XML documents or in
producing DOM trees .

%prep
%setup -q -n XML-Generator-1.13

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

