%define debug_package %{nil}
%global pname wrappers
%global sname wrappers
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	0.3.1
Release:	1PIGSTY%{?dist}
Summary:	Postgres Foreign Data Wrappers by Supabase
License:	Apache-2.0
URL:		https://github.com/supabase/%{sname}
#           https://github.com/supabase/wrappers/archive/refs/tags/v0.3.1.tar.gz

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server

%description
This is a collection of FDWs built by Supabase. We currently support the following FDWs, with more are under development:

HelloWorld: A demo FDW to show how to develop a basic FDW.
BigQuery: A FDW for Google BigQuery which supports data read and modify.
Clickhouse: A FDW for ClickHouse which supports data read and modify.
Stripe: A FDW for Stripe API which supports data read and modify.
Firebase: A FDW for Google Firebase which supports data read only.
Airtable: A FDW for Airtable API which supports data read only.
S3: A FDW for AWS S3. Currently read-only.
Logflare: A FDW for Logflare which supports data read only.
Auth0: A FDW for Auth0.
Cognito: A FDW for AWS Cogntio.
SQL Server: A FDW for Microsoft SQL Server which supports data read only.
Redis: A FDW for Redis which supports data read only.

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/wrappers_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/wrappers-%{version}.so %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/wrappers_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/wrappers-*.sql %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/wrappers_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/wrappers.control %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}-%{version}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id

%changelog
* Sun May 5 2024 Vonng <rh@vonng.com> - 0.3.1
- Initial RPM release, used by Pigsty <https://pigsty.io>