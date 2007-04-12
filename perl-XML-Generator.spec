%define	module 	XML-Generator
%define	name	perl-%{module}
%define version	0.99
%define release %mkrel 2

Summary:	A module to help in generating XML documents from perl
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel >= 5.6
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
%{module} is a module to help in generating XML documents or in
producing DOM trees .

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall_std}
%{__rm} -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%clean 
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes 
%{perl_vendorlib}/XML/*
%{_mandir}/man3/*

