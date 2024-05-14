%define debug_package %{nil}
%global pname pg_lakehouse
%global sname pg_lakehouse
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	0.7.0
Release:	1PIGSTY%{?dist}
Summary:	Query engine over object stores like S3 and table formats like Delta Lake
License:	GNU Affero General Public License v3.0
URL:		https://github.com/paradedb/paradedb/tree/dev/%{sname}

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server

%description
pg_lakehouse is an extension that transforms Postgres into an analytical query engine over object stores like S3 and table formats like Delta Lake.
Queries are pushed down to Apache DataFusion, which delivers excellent analytical performance. Combinations of the following object stores, table formats, and file formats are supported.

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/pg_lakehouse_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/pg_lakehouse.so %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/pg_lakehouse_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_lakehouse*.sql %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/pg_lakehouse_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_lakehouse.control %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id

%changelog
* Sat May 15 2024 Vonng <rh@vonng.com> - 0.7.0
- Initial RPM release, used by Pigsty <https://pigsty.io>