%define	upstream_name 	 XML-Generator
%define upstream_version 1.04

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary:	A module to help in generating XML documents from perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} is a module to help in generating XML documents or in
producing DOM trees .

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
