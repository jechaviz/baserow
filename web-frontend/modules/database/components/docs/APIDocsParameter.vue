<template>
  <li class="api-docs__parameter">
    <div class="api-docs__parameter-name">
      <div>{{ name }}</div>
      <div v-if="optional" class="api-docs__parameter-optional">optional</div>
    </div>
    <div class="api-docs__parameter-description">
      <code class="api-docs__code">{{ type }}</code>
      <div v-if="standard !== ''" class="api-docs__parameter-default">
        Default: {{ standard }}
      </div>
      <div class="api-docs__parameter-content">
        {{ description }}
      </div>
    </div>
  </li>
</template>

<script>
export default {
  name: 'APIDocsParameter',
  props: {
    name: {
      type: String,
      required: true,
    },
    optional: {
      type: Boolean,
      required: false,
      default: false,
    },
    type: {
      type: String,
      required: true,
    },
    standard: {
      type: String,
      required: false,
      default: '',
    },
    description: {
      type: String,
      required: false,
      default: '',
    },
  },
}
</script>
