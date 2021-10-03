module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    'plugin:react/recommended',
    'airbnb',
  ],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 12,
    sourceType: 'module',
  },
  plugins: [
    'react',
  ],
  rules: { // suppress errors for missing 'import React' in files
    'react/react-in-jsx-scope': 'off',
    // allow jsx syntax in js files (for next.js project)
    'react/jsx-filename-extension': [1, {
      extensions: ['.js', '.jsx'],
    }],
    'react/heading-has-content': [1, {
      extensions: ['.js', '.jsx'],
    }],
    'react/button-has-type': 'off',
    'jsx-a11y/heading-has-content': 'off',
    'no-param-reassign': 'off',
    'import/no-extraneous-dependencies ': 'off',
    'react/prop-types': 'off',
  },
};
