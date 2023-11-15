export default {
  global: {
    label: 'label label-text text-base',
    inner: 'my-0.5',
    help: 'px-1 text-xs',
    messages: 'list-none px-1 mt-1 mb-0',
    message: 'font-semibold mb-1',
  },
  email: textClassification,
  password: textClassification,
  submit: submitClassification,
  tel: textClassification,
  text: textClassification,
  textarea: {
    ...errorTheme,
    input: `textarea textarea-bordered resize-none w-full h-48 text-base shadow
    focus:outline-blue-500
    focus:outline-2
    formkit-invalid:border-red-200
    formkit-invalid:shadow-red-200`,
  },
};
