%define debug_package %{nil}
%global pname pgml
%global sname postgresml
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{pname}_%{pgmajorversion}
Version:	2.8.1
Release:	1PIGSTY%{?dist}
Summary:	PostgresML is a complete MLOps platform in a PostgreSQL extension. Build simpler, faster and more scalable models right inside your database.
License:	MIT license
URL:		https://github.com/postgresml/postgresml
Requires:	postgresql%{pgmajorversion}-server

%description
PostgresML is a machine learning extension for PostgreSQL that enables you to perform training and inference on text and tabular data using SQL queries.
 With PostgresML, you can seamlessly integrate machine learning models into your PostgreSQL database and harness the power of cutting-edge algorithms to process data efficiently.

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/usr
cp -a ~/rpmbuild/SOURCES/pgml_%{pgmajorversion}/usr/* $RPM_BUILD_ROOT/usr/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id/*

%changelog
* Fri Jan 19 2024 Vonng <rh@vonng.com> - 2.8.1
- Bump version to v2.8.1 with PG 16 support
* Mon Sep 18 2023 Vonng <rh@vonng.com> - 2.7.9
- Initial RPM release, used by Pigsty <https://pigsty.cc>