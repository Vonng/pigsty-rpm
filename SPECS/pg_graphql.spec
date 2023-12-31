%define debug_package %{nil}
%global pname pg_graphql
%global sname pg_graphql
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	1.4.0
Release:	1PIGSTY%{?dist}
Summary:	GraphQL support to your PostgreSQL database.
License:	Apache-2.0
URL:		https://github.com/supabase/%{sname}
Source0:	https://github.com/supabase/%{sname}/archive/refs/tags/%{version}.tar.gz
#           https://github.com/supabase/pg_graphql/archive/refs/tags/v1.4.0.tar.gz

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server

%description
pg_graphql reflects a GraphQL schema from the existing SQL schema.
The extension keeps schema translation and query resolution neatly contained on your database server.
This enables any programming language that can connect to PostgreSQL to query the database via GraphQL with no additional servers, processes, or libraries.

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/pg_graphql-pg%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/pg_graphql.so %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/pg_graphql-pg%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_graphql--1.4.0.sql %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/pg_graphql-pg%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_graphql.control %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id

%changelog
* Wed Oct 11 2023 Vonng <rh@vonng.com> - 1.4.0
- Bump version to v1.4.0
* Mon Sep 18 2023 Vonng <rh@vonng.com> - 1.3.0
- Initial RPM release, used by Pigsty <https://pigsty.cc>