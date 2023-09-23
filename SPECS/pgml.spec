%define debug_package %{nil}
%global pname pgml
%global sname postgresml
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	2.7.9
Release:	PIGSTY1%{?dist}
Summary:	pgml adds GraphQL support to your PostgreSQL database.
License:	Apache-2.0
URL:		https://github.com/%{postgresml}/%{postgresml}
#Source0:	https://github.com/%{postgresml}/%{postgresml}/archive/refs/tags/v%{version}.tar.gz
#           https://github.com/postgresml/postgresml/archive/refs/tags/v2.7.9.tar.gz

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server

%description
PostgresML is a machine learning extension for PostgreSQL that enables you to perform training and inference on text and tabular data using SQL queries.
 With PostgresML, you can seamlessly integrate machine learning models into your PostgreSQL database and harness the power of cutting-edge algorithms to process data efficiently.

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/%{pname}-pg%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/pgml.so                     %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/%{pname}-pg%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pgm*.sql        %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/%{pname}-pg%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pgml.control    %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql

%changelog
* Mon Sep 18 2023 Vonng <rh@vonng.com> - 2.7.9
- Initial RPM release, used by Pigsty <https://pigsty.cc>