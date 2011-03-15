%define	rname	actionpack

Summary:	Part of Rails framework handling controller/view split
Name:		ruby-%{rname}
Version:	2.3.11
Release:	%mkrel 1
URL:		http://www.rubyonrails.com/
Source0:	http://rubygems.org/gems/%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems 
Provides:	rubygem(%{rname})

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

%build

%install
rm -rf %buildroot
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache
chmod g-w,g+r,o+r -R %{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec
