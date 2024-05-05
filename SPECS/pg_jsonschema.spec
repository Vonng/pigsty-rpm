%define debug_package %{nil}
%global pname pg_jsonschema
%global sname pg_jsonschema
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	0.3.1
Release:	1PIGSTY%{?dist}
Summary:	PostgreSQL extension providing JSON Schema validation
License:	Apache-2.0
URL:		https://github.com/supabase/%{sname}
#           https://github.com/supabase/pg_jsonschema/archive/refs/tags/v0.3.1.tar.gz

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server

%description
pg_jsonschema reflects a GraphQL schema from the existing SQL schema.
The extension keeps schema translation and query resolution neatly contained on your database server.
This enables any programming language that can connect to PostgreSQL to query the database via GraphQL with no additional servers, processes, or libraries.

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/pg_jsonschema_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/pg_jsonschema.so %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/pg_jsonschema_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_jsonschema-*.sql %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/pg_jsonschema_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_jsonschema.control %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id

%changelog
* Sun May 5 2024 Vonng <rh@vonng.com> - 0.3.1
- Initial RPM release, used by Pigsty <https://pigsty.io>