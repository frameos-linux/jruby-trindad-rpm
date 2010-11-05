%define ruby_sitelib %(jruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(jruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname trinidad
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Simple library to run rails applications into an embedded Tomcat
Name: jruby-%{gemname}
Version: 1.0.1
Release: 1.frameos
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/calavera/trinidad
Source0: http://gemcutter.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: jruby 
Requires: jruby-trinidad-jars >= 0.3.0
Requires: jruby-rack >= 1.0.2
BuildRequires: jruby 
BuildArch: noarch
Provides: jruby-%{gemname} = %{version}

%description
Trinidad allows you to run a rails or rackup applications within an embedded
Apache Tomcat container


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
jgem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/trinidad
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/LICENSE
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Fri Nov 05 2010 : Sergio Rubio <rubiojr@frameos.org> - 1.0.1-1
-  updated to trinidad 1.0.1

* Fri Oct 15 2010 : Sergio Rubio <rubiojr@frameos.org> - 0.9.10-1
- Initial package
