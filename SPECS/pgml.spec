%define debug_package %{nil}
%global pname pgml
%global sname postgresml
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{pname}_%{pgmajorversion}
Version:	2.7.9
Release:	1PIGSTY%{?dist}
Summary:	pgml adds GraphQL support to your PostgreSQL database.
License:	Apache-2.0
URL:		https://github.com/postgresml/postgresml
Requires:	postgresql%{pgmajorversion}-server

%description
PostgresML is a machine learning extension for PostgreSQL that enables you to perform training and inference on text and tabular data using SQL queries.
 With PostgresML, you can seamlessly integrate machine learning models into your PostgreSQL database and harness the power of cutting-edge algorithms to process data efficiently.

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/usr
cp -a ~/rpmbuild/SOURCES/pgml_15/usr/* $RPM_BUILD_ROOT/usr/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id/*

%changelog
* Mon Sep 18 2023 Vonng <rh@vonng.com> - 2.7.9
- Initial RPM release, used by Pigsty <https://pigsty.cc>