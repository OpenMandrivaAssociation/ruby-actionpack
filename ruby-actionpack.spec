%define rname actionpack
%define name ruby-%{rname}
%define version 1.12.5
%define release %mkrel 1

Summary:	Part of Rails framework handling controller/view split
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.rubyonrails.com/
Source0:	%{rname}-%{version}.gem
# (blino) from http://dev.rubyonrails.org/ticket/6513
Patch0:		actionpack-1.12.5-rdoc.patch
License:	MIT
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Requires:	ruby 
BuildRequires:	ruby-RubyGems 

%description
Action Pack splits the response to a web request into a controller part
(performing the logic) and a view part (rendering a template). This two-step
approach is known as an action, which will normally create, read, update, or
delete (CRUD for short) some sort of model part (often backed by a database)
before choosing either to render a template or redirecting to another action.

Action Pack implements these actions as public methods on Action Controllers
and uses Action Views to implement the template rendering. Action Controllers
are then responsible for handling all the actions relating to a certain part
of an application. This grouping usually consists of actions for lists and for
CRUDs revolving around a single (or a few) model objects. So ContactController
would be responsible for listing contacts, creating, deleting, and updating
contacts. A WeblogController could be responsible for both posts and comments.

Action View templates are written using embedded Ruby in tags mingled in with
the HTML. To avoid cluttering the templates with code, a bunch of helper
classes provide common behavior for forms, dates, and strings. And it's easy
to add specific helpers to keep the separation as the application evolves.

Note: Some of the features, such as scaffolding and form building, are tied to
ActiveRecord[http://activerecord.rubyonrails.org] (an object-relational
mapping package), but that doesn't mean that Action Pack depends on Active
Record. Action Pack is an independent package that can be used with any sort
of backend (Instiki[http://www.instiki.org], which is based on an older version
of Action Pack, used Madeleine for example). Read more about the role Action
Pack can play when used together with Active Record on
http://www.rubyonrails.org.

%prep
rm -rf %rname-%version
rm -rf tmp-%rname-%version
mkdir tmp-%rname-%version
gem install --ignore-dependencies %{SOURCE0} --no-rdoc --install-dir `pwd`/tmp-%rname-%version
mv tmp-%rname-%version/gems/%rname-%version .
mv tmp-%rname-%version/specifications/%rname-%version.gemspec %rname-%version/
rm -rf tmp-%rname-%version
%setup -T -D -n %rname-%version
%patch0 -p1 -b .rdoc

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
chmod 0644 README

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT{%{ruby_sitelibdir},%{ruby_ridir},%{ruby_gemdir}/specifications}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_sitelibdir}
cp -a ri/ri/{ActionController,ActionView,CGIMethods} $RPM_BUILD_ROOT%{ruby_ridir}
cp -a %rname-%version.gemspec $RPM_BUILD_ROOT%{ruby_gemdir}/specifications/

for f in `find %buildroot%{ruby_sitelibdir} examples -type f`
do
        if head -n1 "$f" | grep '^#!' >/dev/null;
        then
                sed -i 's|/usr/local/bin|/usr/bin|' "$f"
                chmod 0755 "$f"
        else
                chmod 0644 "$f"
        fi
done


%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/*
%{ruby_ridir}/*
%{ruby_gemdir}/specifications/%rname-%version.gemspec
%doc CHANGELOG README rdoc examples


