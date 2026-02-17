'use client';

import AuthSplit from '@/components/boilerplates/AuthSplit';

export default function LoginPage() {
  return (
    <AuthSplit
      mode="login"
      title="Welcome back"
      subtitle="Sign in to your Enterprise OS account"
      fields={[
        { key: 'email', label: 'Email', type: 'email', placeholder: 'john@company.com', required: true },
        { key: 'password', label: 'Password', type: 'password', placeholder: 'Enter your password', required: true },
      ]}
      submitLabel="Sign in"
      onSubmit={(values) => console.log('Login:', values)}
      ssoProviders={[
        { name: 'Google', onClick: () => console.log('Google SSO') },
        { name: 'Microsoft', onClick: () => console.log('Microsoft SSO') },
      ]}
      footerLinks={[
        { label: "Don't have an account? Register", href: '/register' },
      ]}
    />
  );
}
