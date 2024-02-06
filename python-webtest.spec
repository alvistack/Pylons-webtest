# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-webtest
Epoch: 100
Version: 3.0.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Helper to test WSGI applications
License: MIT
URL: https://github.com/Pylons/webtest/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This wraps any WSGI application and makes it easy to send test requests
to that application, without starting up an HTTP server.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-WebTest
Summary: Helper to test WSGI applications
Requires: python3
Requires: python3-beautifulsoup4
Requires: python3-waitress >= 0.8.5
Requires: python3-WebOb >= 1.2
Provides: python3-webtest = %{epoch}:%{version}-%{release}
Provides: python3dist(webtest) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-webtest = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(webtest) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-webtest = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(webtest) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-WebTest
This wraps any WSGI application and makes it easy to send test requests
to that application, without starting up an HTTP server.

%files -n python%{python3_version_nodots}-WebTest
%license license.rst
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-WebTest
Summary: Helper to test WSGI applications
Requires: python3
Requires: python3-beautifulsoup4
Requires: python3-waitress >= 0.8.5
Requires: python3-WebOb >= 1.2
Provides: python3-webtest = %{epoch}:%{version}-%{release}
Provides: python3dist(webtest) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-webtest = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(webtest) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-webtest = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(webtest) = %{epoch}:%{version}-%{release}

%description -n python3-WebTest
This wraps any WSGI application and makes it easy to send test requests
to that application, without starting up an HTTP server.

%files -n python3-WebTest
%license license.rst
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-webtest
Summary: Helper to test WSGI applications
Requires: python3
Requires: python3-beautifulsoup4
Requires: python3-waitress >= 0.8.5
Requires: python3-webob >= 1.2
Provides: python3-webtest = %{epoch}:%{version}-%{release}
Provides: python3dist(webtest) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-webtest = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(webtest) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-webtest = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(webtest) = %{epoch}:%{version}-%{release}

%description -n python3-webtest
This wraps any WSGI application and makes it easy to send test requests
to that application, without starting up an HTTP server.

%files -n python3-webtest
%license license.rst
%{python3_sitelib}/*
%endif

%changelog
