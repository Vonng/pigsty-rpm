
## 扩展编译

如果您想要的扩展包不在 Pigsty 中，也不在 [PGDG](https://download.postgresql.org/pub/repos/yum/) 官方源里，那么您可以考虑编译安装，或者将编译好的扩展打包成 RPM 包分发。

想要编译扩展，您需要安装 `rpmbuild`，`gcc/clang`，以及其他相关的 `-devel` 软件包，特别是您还需要 `pgdg-srpm-macros` 来构建标准的 PGDG 式扩展 RPM。

完整安装完毕的 Pigsty 的三节点构建环境 [`build.yml`](https://github.com/Vonng/pigsty/blob/master/files/pigsty/full.yml) 可以作为编译环境的基础，您可以在此环境中安装编译所需的依赖：

```bash
make build check-repo install    # 创建一个 3 节点构建环境，拷贝离线软件包，并进行完整初始化。
bin/repo-add infra node,pgsql    # 将上游的操作系统/PostgreSQL源加入到3台INFRA节点的本地yum源中

# 您还需要将 SRPM 的仓库添加至机器的yum源中
cat > /etc/yum.repos.d/pgdg-srpm.repo <<-'EOF'
[pgdg-common-srpm]
name = PostgreSQL 15 SRPM $releasever - $basearch
baseurl=https://download.postgresql.org/pub/repos/yum/srpms/common/redhat/rhel-$releasever-x86_64/
gpgcheck = 0
enabled = 1
module_hotfixes=1
EOF

# 安装编译工具，构建依赖，以及 PostgreSQL 各大版本
yum groupinstall -y 'Development Tools' --nobest
yum install -y pgdg-srpm-macros clang ccache rpm-build rpmdevtools postgresql1*-server flex bison libxml2-devel CUnit cmake postgresql1*-devel readline-devel zlib-devel lz4-devel libzstd-devel openssl-devel krb5-devel libcurl-devel gd-devel 
rpmdev-setuptree  # 初始化 rpm 构建目录结构
```

下面是编译一个 PostgreSQL 扩展 `pgsql-http` 的说明：首先撰写软件包的规格说明文件，放置于： `/root/rpmbuild/SPECS/pgsql-http.spec`。

<details><summary>示例：构建 http 扩展的 RPM SPEC</summary>

```
%global pname http
%global sname pgsql-http
%global pginstdir /usr/pgsql-%{pgmajorversion}

%ifarch ppc64 ppc64le s390 s390x armv7hl
 %if 0%{?rhel} && 0%{?rhel} == 7
  %{!?llvm:%global llvm 0}
 %else
  %{!?llvm:%global llvm 1}
 %endif
%else
 %{!?llvm:%global llvm 1}
%endif

Name:		%{sname}_%{pgmajorversion}
Version:	1.6.0
Release:	1PIGSTY%{?dist}
Summary:	HNSW algorithm for vector similarity search in PostgreSQL.
License:	MIT
URL:		https://github.com/pramsey/%{sname}
Source0:	https://github.com/pramsey/%{sname}/archive/refs/tags/v%{version}.tar.gz
#           https://github.com/pramsey/pgsql-http/archive/refs/tags/v1.6.0.tar.gz

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server

%description
Wouldn't it be nice to be able to write a trigger that called a web service? Either to get back a result,
 or to poke that service into refreshing itself against the new state of the database? This extension is for that.


%if %llvm
%package llvmjit
Summary:	Just-in-time compilation support for %{sname}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} == 7
%ifarch aarch64
Requires:	llvm-toolset-7.0-llvm >= 7.0.1
%else
Requires:	llvm5.0 >= 5.0
%endif
%endif
%if 0%{?suse_version} >= 1315 && 0%{?suse_version} <= 1499
BuildRequires:	llvm6-devel clang6-devel
Requires:	llvm6
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:	llvm15-devel clang15-devel
Requires:	llvm15
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:	llvm => 13.0
%endif

%description llvmjit
This packages provides JIT support for %{sname}
%endif


%prep
%setup -q -n %{sname}-%{version}

%build
PATH=%{pginstdir}/bin:$PATH %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
PATH=%{pginstdir}/bin:$PATH %{__make} %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
%doc README.md
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%if %llvm
%files llvmjit
   %{pginstdir}/lib/bitcode/*
%endif

%changelog
* Wed Sep 13 2023 Vonng <rh@vonng.com> - 1.6.0
- Initial RPM release, used by Pigsty <https://pigsty.cc>
```

</details>

您可以将该扩展的源码包下载至`/root/rpmbuild/SOURCES`，然后使用 `rpmbuild` 命令针对不同的PG大版本进行编译：

```bash
rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/pgsql-http.spec;
rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/pgsql-http.spec;
rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/pgsql-http.spec;
rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/pgsql-http.spec;
rpmbuild --define "pgmajorversion 12" -ba ~/rpmbuild/SPECS/pgsql-http.spec;
```

编译成果会放置在 `/root/rpmbuild/RPMS`，将其移动到 Pigsty 本地源 `/www/pigsty`，并执行 `./infra.yml -t repo_create` 重建本地源。
您可能还需要清空使用本地仓库的其他节点上的本地 Yum 缓存：`ansible all -b -a 'yum clean all'`。

这样，您就可以在其他主机上使用编译好的扩展 RPM 包了。具体细节请参考 rpm 构建资料，不再展开。



## RUST 编译环境配置


```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

```