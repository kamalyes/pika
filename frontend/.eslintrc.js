module.exports = {
  rules: {
    'no-console': 'off',
    'no-debugger': 'off',
    'space-before-function-paren': ['error', 'never'],
    // 是否逗号结尾 never: 从不
    'comma-dangle': [0, 'never'],
    // 是否分号结尾
    semi: [0, 'never'],
    // 单引号还是双引号字符串
    quotes: [0, 'single'],
    // 方法前是否要一个空格 always: 总是要
    'space-before-function-paren': [0, 'never'],
    '@typescript-eslint/no-explicit-any': 'off',
    '@typescript-eslint/no-empty-function': 'off',
    '@typescript-eslint/no-unused-vars': 'off',
    '@typescript-eslint/camelcase': 'off',
    '@typescript-eslint/no-this-alias': 'off',
  },
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint'],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react/recommended',
    'plugin:jest/recommended',
    'prettier',
    'prettier/@typescript-eslint',
  ],
  rules: {
    'react/prop-types': false,
  },
  parserOptions: {
    ecmaVersion: 6,
    project: './tsconfig.json',
    sourceType: 'module',
  },
  settings: {
    react: {
      version: 'detect',
    },
    linkComponents: [{ name: 'Link', linkAttribute: 'href' }],
  },
  env: {
    browser: true,
  },
  globals: {
    ANT_DESIGN_PRO_ONLY_DO_NOT_USE_IN_YOUR_PRODUCTION: true,
    page: true,
    REACT_APP_ENV: true,
  },
};
